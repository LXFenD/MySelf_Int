from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.serializers import IntegerField
from .models import Category, Blog, Tags_Time


class CateSerializer(ModelSerializer):
    """
    序列化对象
    """

    class Meta:
        model = Category
        fields = ['cate_name', 'cate_date', 'id']


class Tages_Time_Serializer(ModelSerializer):
    class Meta:
        model = Tags_Time
        fields = ['id', 'tag_time']

class Tages_Time_Serializer_Num(ModelSerializer):
    num = IntegerField()
    class Meta:
        model = Tags_Time
        fields = ['id', 'tag_time','num']


class CateSerializer_Num(ModelSerializer):
    """
    序列化对象
    """
    num = IntegerField()

    class Meta:
        model = Category
        fields = ['cate_name', 'cate_date', 'id', 'num']


class BlogSerializer(ModelSerializer):
    """
    序列化BLog对象
    """
    blog_cate = CateSerializer()

    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_detail', 'blog_content',
                  'blog_image', 'blog_date', 'blog_cate', 'id',
                  'blog_zan', 'blog_readnum', 'blog_video_url',
                  'blog_tage_time'
                  ]
