from django.urls import path,include
from . import views
urlpatterns = [

    path('all/',views.get_all),
    path('cate/all/',views.get_cate_all),
    path('load/img/',views.upload_load_img),
    path('qiniu/img/',views.upload_qiniu_img),
    path('six_bg/',views.get_six_blog),
    path('save/',views.insert_blog),
    path('read_bg/',views.get_read_blog),
    path('play_id/',views.get_play_ping),
    path('play_info/',views.get_play_info),
    path('save_img/',views.save_img_aliyun),
    path('video_list/',views.get_video_list),

]