import os
import time
import qiniu
from datetime import datetime
from django.conf import settings
from django.utils.timezone import make_aware
from utils.rest_api import ok, param_error, server_error
from .models import  Category,Blog
from .serializer import BlogSerializer,CateSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET,require_POST,require_http_methods
import json
import oss2
from aliyunsdkvod.request.v20170321 import GetVideoPlayAuthRequest,GetPlayInfoRequest,GetVideoListRequest
from aliyunsdkcore import client
clt = client.AcsClient(settings.ALIYUN_PLAY_ACCESS_KEY_ID,settings.ALIYUN_PLAY_ACCESS_KEY_SECRET,'cn-shanghai')
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
    data = BlogSerializer(blogs,many=True).data
    return ok(data=data)

@require_GET
def get_cate_all(request):
    cates = Category.objects.all()
    data = CateSerializer(cates,many=True).data
    return ok(data=data)


@csrf_exempt
@require_http_methods(['POST','OPTIONS'])
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
            dir_time = str(make_aware(datetime.now())).split(' ')[0]
            dir = settings.MEDIA_ROOT+'/'+dir_time
            try:
                os.makedirs(dir)
            except:
                pass

            img_name = '{}'.format(int(time.time()))+'.'+img_type
            with open(dir+'/'+img_name,'wb') as fp:
                for img in file.chunks():
                    fp.write(img)
            img_url = settings.JIEKOU+ 'media/'+dir_time+'/'+img_name
            return ok(data={'img_url':img_url})
        else:
            return param_error()
    else:
        return ok()


@csrf_exempt
@require_http_methods(['POST','OPTIONS'])
def upload_qiniu_img(request):
    """
    上传图片到七牛云
    :param request:
    :return:
    """
    AccessKey = 'T8eCm8UaAFpVKUZ90btOs3m95OiIT4O8Ji5eMKCB'
    SecretKey = 'NxtbTVgFLm0CWmOos1hD5M0EbwQj-6-VnB-KD7Z2'
    q= qiniu.Auth(AccessKey,SecretKey)
    bucket_name = 'xxxfffzzz'
    name = 'http://cdn.odinhj.cn'
    token = q.upload_token(bucket_name)
    if token:
        return ok(data={'token':token,'url':name})
    else:
        return server_error()


@csrf_exempt
@require_http_methods(['POST','OPTIONS'])
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
    data = BlogSerializer(blogs,many=True).data
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
    print(video_id)
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
@require_http_methods(['POST','OPTIONS'])
def save_img_aliyun(request):
    """
    上传图片地址：并返回图片上传的url
    由于是外网访问阿里云oss，所以需要设置url地址的访问时间  默认设置为10年
    :param request:
    :return:JSONResponse
    """
    if request.method =="POST":
        file = request.FILES.get('file')
        auth = oss2.Auth(settings.ALIYUN_PLAY_ACCESS_KEY_ID,settings.ALIYUN_PLAY_ACCESS_KEY_SECRET)
        buck = oss2.Bucket(auth,'http://oss-cn-hangzhou.aliyuncs.com','ms-lmyself')
        type = str(file.name).split('.')[-1]
        img_name = str(int(time.time()))+'.'+type
        buck.put_object(img_name,file)
        url = buck.sign_url('GET',img_name,3600*1000*24*365*10)
        url = str(url).replace('ms-lmyself.oss-cn-hangzhou.aliyuncs.com','image.odinhj.cn')
        return ok(data={'img_url':url})
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