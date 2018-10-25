from rest_framework.serializers import Serializer, ModelSerializer
from .models import Category, Blog


class CateSerializer(ModelSerializer):
    """
    序列化对象
    """

    class Meta:
        model = Category
        fields = ['cate_name', 'cate_date', 'id']


class BlogSerializer(ModelSerializer):
    """
    序列化BLog对象
    """
    blog_cate = CateSerializer()

    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_detail', 'blog_content',
                  'blog_image', 'blog_date', 'blog_cate', 'id',
                  'blog_zan', 'blog_readnum','blog_video_url'
                  ]
