import os
import time
import qiniu
import datetime
from django.conf import settings
from django.utils.timezone import make_aware
from utils.rest_api import ok, param_error, server_error
from .models import Category, Blog, Tags_Time
from .serializer import BlogSerializer, CateSerializer, CateSerializer_Num, Tages_Time_Serializer_Num
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
import json

import oss2
from django.utils import timezone
from django.db.models import Avg, Count
from aliyunsdkvod.request.v20170321 import GetVideoPlayAuthRequest, \
    GetPlayInfoRequest, GetVideoListRequest, CreateUploadVideoRequest, RefreshUploadVideoRequest
from aliyunsdkcore import client

clt = client.AcsClient(settings.ALIYUN_PLAY_ACCESS_KEY_ID, settings.ALIYUN_PLAY_ACCESS_KEY_SECRET, 'cn-shanghai')


# Create your views here
@csrf_exempt
# @require_http_methods(['POST','OPTIONS'])
@require_GET
def get_all(request):
    """
    获取所有的文章信息
    :param request:
    :return:
    """
    blogs = Blog.objects.all()
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_cate_all(request):
    """
    获取所有分类
    :param request:
    :return:
    """
    cates = Category.objects.all()
    data = CateSerializer(cates, many=True).data
    return ok(data=data)


@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def upload_load_img(request):
    """
    上传图片到服务器
    :param request:
    :return:
    """
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:

            img_type = file.name.split('.')[-1]
            dir_time = str(make_aware(datetime.datetime.now())).split(' ')[0]
            dir = settings.MEDIA_ROOT + '/' + dir_time
            try:
                os.makedirs(dir)
            except:
                pass

            img_name = '{}'.format(int(time.time())) + '.' + img_type
            with open(dir + '/' + img_name, 'wb') as fp:
                for img in file.chunks():
                    fp.write(img)
            img_url = settings.JIEKOU + 'media/' + dir_time + '/' + img_name
            return ok(data={'img_url': img_url})
        else:
            return param_error()
    else:
        return ok()


@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def upload_qiniu_img(request):
    """
    上传图片到七牛云
    :param request:
    :return:
    """
    AccessKey = 'T8eCm8UaAFpVKUZ90btOs3m95OiIT4O8Ji5eMKCB'
    SecretKey = 'NxtbTVgFLm0CWmOos1hD5M0EbwQj-6-VnB-KD7Z2'
    q = qiniu.Auth(AccessKey, SecretKey)
    bucket_name = 'xxxfffzzz'
    name = 'http://cdn.odinhj.cn'
    token = q.upload_token(bucket_name)
    if token:
        return ok(data={'token': token, 'url': name})
    else:
        return server_error()


@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def insert_blog(request):
    """
    前段返回来的数据字段:
    blog_title:  文章标题
    blog_detail: 文章描述
    blog_content: 文章内容
    blog_category_id: 文章分类
    blog_user_uuid: 文章作者
    存储博客
    :param request:
    :return: json
    """
    if request.method == 'POST':
        try:
            blog_title = request.POST.get('blog_title')
            blog_detail = request.POST.get('blog_detail')
            blog_content = request.POST.get('blog_content')
            blog_category_id = request.POST.get('blog_category_id')
            blog_img = request.POST.get('blog_img')
            blog_cate = Category.objects.get(pk=int(blog_category_id))
            blog = Blog.objects.create(blog_name=blog_title,
                                       blog_detail=blog_detail,
                                       blog_content=blog_content,
                                       blog_cate=blog_cate,
                                       blog_image=blog_img)
        except:
            return param_error()
        if blog:
            return ok()
        else:
            return param_error()
    return ok()


@require_GET
def get_six_blog(request):
    """
    获取六篇最新数据
    :param request:
    :return:
    """
    blogs = Blog.objects.all()[0:6]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_read_blog(request):
    """
    获取阅读最多
    :param request:
    :return:
    """
    blogs = Blog.objects.all().order_by("-blog_readnum")[0:6]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_play_ping(request):
    """
    获取视频播放凭证
    :param request:
    :return:
    """
    requests = GetVideoPlayAuthRequest.GetVideoPlayAuthRequest()
    requests.set_accept_format('JSON')
    requests.set_VideoId("7e2ed158d0924d3b8a2da293818642bb")
    response = json.loads(clt.do_action(requests))
    # playAuth = response.get('PlayAuth')

    return ok(data=response)


@require_GET
def get_play_info(request):
    """
    获取视频播放凭证
    :param request:
    :return:
    """
    video_id = request.GET.get('video_id')
    if video_id:
        requests = GetPlayInfoRequest.GetPlayInfoRequest()
        requests.set_accept_format('JSON')
        requests.set_VideoId(video_id)
        response = json.loads(clt.do_action(requests))
        # playAuth = response.get('PlayAuth')
        return ok(data=response)
    else:
        return param_error()


@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def save_img_aliyun(request):
    """
    上传图片地址：并返回图片上传的url
    由于是外网访问阿里云oss，所以需要设置url地址的访问时间  默认设置为10年
    :param request:
    :return:JSONResponse
    """
    if request.method == "POST":
        file = request.FILES.get('file')
        auth = oss2.Auth(settings.ALIYUN_PLAY_ACCESS_KEY_ID, settings.ALIYUN_PLAY_ACCESS_KEY_SECRET)
        buck = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'ms-lmyself')
        type = str(file.name).split('.')[-1]
        img_name = str(int(time.time())) + '.' + type
        buck.put_object(img_name, file)
        url = buck.sign_url('GET', img_name, 3600 * 1000 * 24 * 365 * 10)
        url = str(url).replace('ms-lmyself.oss-cn-hangzhou.aliyuncs.com', 'image.odinhj.cn')
        return ok(data={'img_url': url})
    else:
        return ok()


@require_GET
def get_video_list(request):
    """
    获取所有的视频列表
    :param request:
    :return:
    """
    requests = GetVideoListRequest.GetVideoListRequest()
    requests.set_accept_format('JSON')
    response = json.loads(clt.do_action(requests))
    return ok(data=response)


@require_GET
def zhan_rem(request):
    """
    站长推荐文章-banner
    :param request:
    :return:
    """
    blogs = Blog.objects.select_related("blog_cate").order_by('-blog_zan').all()[0:4]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_time_blog(request):
    """
    根据月份获取博客的个数：
    :param request:
    :return:
    """
    blogs = Tags_Time.objects.annotate(num=Count("blog"))
    data = Tages_Time_Serializer_Num(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_cate_blog(request):
    """
    统计获取博客类型
    :param request:
    :return:
    """
    blogs = Category.objects.annotate(num=Count("blog"))
    data = CateSerializer_Num(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_month(request):
    """
    根据月份归档每月编写的博客数量
    :param request:
    :return:
    """
    blog_times = Blog.objects.datetimes('blog_date', 'month', "DESC")
    apps = []
    times_nums = []
    for i in blog_times:
        blog = Blog.objects.filter(blog_date__year=i.year, blog_date__month=i.month).count()
        apps.append(i.year)
        apps.append(i.month)
        apps.append(blog)
        times_nums.append(apps)
        apps = []
    return ok(data=times_nums)


@require_GET
def sort_time_re(request):
    """
    根据时间热度排序获取前六条数据
    :param request:
    :return:
    """
    blogs = Blog.objects.select_related('blog_cate').order_by('-blog_date', '-blog_readnum')[0:6]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def re_rem(request):
    """
    根据观看进行排序获取前六
    :param request:
    :return:
    """
    blogs = Blog.objects.select_related('blog_cate').all().order_by('-blog_readnum')[0:6]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def lv_rem(request):
    """
    根据点赞数进行排序获取前六
    :param request:
    :return:
    """
    blogs = Blog.objects.select_related('blog_cate').all().order_by('-blog_zan')[0:6]
    data = BlogSerializer(blogs, many=True).data
    return ok(data=data)


@require_GET
def get_cate_id_blog(request):
    """
    根据分类id获取博客文章
    如果cate_id ==0:
        就是获取所有的文章
    :param request:
    :return:
    """
    cate_id = request.GET.get('cate_id')
    if cate_id:
        if int(cate_id) == 0:
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(blog_cate__id=int(cate_id))
        data = BlogSerializer(blogs, many=True).data
        return ok(data=data)
    else:
        return param_error()


@require_GET
def create_upload_video(request):
    """
    上传视频
    创建上传任务
    获取用户的上传凭证和视频的上传信息
    :param request:
    :return:
    """
    vid_name = request.GET.get('vid_name')
    vid_title = request.GET.get('vid_title')
    vid_fenlei = request.GET.get('vid_fenlei')
    if vid_name and vid_title and vid_fenlei:
        vid_detail = request.GET.get('vid_detail')
        vid_tags = request.GET.get('vid_tags')
        vid_coverurl = request.GET.get('vid_coverurl')

        requests = CreateUploadVideoRequest.CreateUploadVideoRequest()
        requests.set_Title(vid_title)  # 视频标题(必填参数)
        requests.set_FileName(vid_name)  # 视频源文件名称，必须包含扩展名(必填参数)
        if vid_detail:
            requests.set_Description(vid_detail)  # 视频描述信息(可选)
        if vid_coverurl:
            requests.set_CoverURL(vid_coverurl)  # 自定义视频封面(可选)，不设置会默认取第一张截图作为封面
        if vid_tags:
            requests.set_Tags(vid_tags)  # 视频标签，多个用逗号分隔(可选)
        requests.set_CateId(int(vid_fenlei))  # 视频分类(可选，可在点播控制台·全局设置·分类管理里查看分类ID：
                                # https://vod.console.aliyun.com/#/vod/settings/category)
        requests.set_accept_format('JSON')
        response = json.loads(clt.do_action(requests))
        print(response)
        return ok(data=response)
    else:
        return param_error()


@require_GET
def refresh_upload_token(request):
    request = RefreshUploadVideoRequest.RefreshUploadVideoRequest()
    request.set_accept_format('JSON')
    request.set_VideoId("d6e2fb63b5e040c4a9ed04830325dff9")
    response = json.loads(clt.do_action(request))
    return ok(data=response)



