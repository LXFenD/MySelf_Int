from django.urls import path,include
from . import views
urlpatterns = [

    path('all/',views.get_all), #获取所有博客
    path('cate/all/',views.get_cate_all), #获取所有分类
    path('load/img/',views.upload_load_img), #上传本地图片
    path('qiniu/img/',views.upload_qiniu_img), #上传到七牛云图片
    path('six_bg/',views.get_six_blog), #获取最新的六篇文章
    path('save/',views.insert_blog), #保存博客
    path('read_bg/',views.get_read_blog), #根据阅读获取博客
    path('play_id/',views.get_play_ping), #获取视频播放id
    path('play_info/',views.get_play_info), #获取视频信息
    path('save_img/',views.save_img_aliyun), #上传图片到阿里云的对象存储
    path('video_list/',views.get_video_list), #获取视频列表
    path('zan_rem/',views.zhan_rem), #根据点赞数获取推荐
    path('month_blog/',views.get_time_blog), #根据月份获取文章
    path('cate_blog_num/',views.get_cate_blog), ##根据分类归档博客
    path('mmm/',views.get_month), #根据月份归档
    path('time_sort/',views.sort_time_re), #按时间排序
    path('re_rem/',views.re_rem), #
    path('lv_rem/',views.lv_rem),
    path('cate_id_bg/',views.get_cate_id_blog),
    path('create_upload_video/',views.create_upload_video),
    path('refresh_upload_token/',views.refresh_upload_token),

]