from django.db import models

# Create your models here.
class Category(models.Model):
    """
    分类表
    """
    cate_name = models.CharField(max_length=100)
    cate_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'
        ordering = ['-cate_date']

class Blog(models.Model):
    """
    博客表
    """
    blog_name = models.CharField(max_length=100)
    blog_detail = models.CharField(max_length=300)
    blog_content = models.TextField()
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_readnum = models.IntegerField(default=0)
    blog_zan = models.IntegerField(default=0)
    blog_image = models.CharField(max_length=500)
    blog_cate = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    blog_video_url = models.CharField(max_length=888,default="")
    class Meta:
        db_table = 'blog'
        ordering = ['-blog_date']