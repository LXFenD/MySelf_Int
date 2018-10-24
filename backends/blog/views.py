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
