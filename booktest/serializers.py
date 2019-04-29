from rest_framework import serializers
from .models import BookInfo, HeroInfo


"""
高级序列化器使用如下：

"""


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""

    class Meta:
        model = BookInfo
        fields = '__all__'  # 过滤所有字段
        # fields = ('id', 'btitle', 'bpub_date')  # 过滤指定字段
        # exclude = ('logo',)

        read_only_fields = ('id', 'bread', 'bcomment')  # 设置序列化只读字段

        extra_kwargs = {
                        'bread': {'min_value': 0, 'required': True},
                        'bcomment': {'min_value': 0, 'required': True},
                        }


class HeroInfoSerializer(serializers.ModelSerializer):
    """英雄数据序列化器"""

    hbook = BookInfoSerializer(many=True)  # 外键自定义处理

    class Meta:
        model = HeroInfo
        # fields = '__all__'
        # depth = 1  # 指定外键关联深度（相当于Serializer类的嵌套写法）

        fields = ('id', 'hname', 'hgender', 'hcontent', 'hbook')

