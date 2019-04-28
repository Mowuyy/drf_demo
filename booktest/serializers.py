from rest_framework import serializers
from .models import BookInfo

"""
序列化器字段说明 => https://www.django-rest-framework.org/api-guide/fields/
"""


# class BookInfoSerializer(serializers.ModelSerializer):
#     """图书数据序列化器"""
#
#     class Meta:  # 元类，元数据表示对该序列化器的约束条件
#         model = BookInfo  # 序列化器与模型类关联
#         fields = '__all__'  # 关联中所被允许访问的字段，all表示所有字段都被允许


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)  # read_only=True 表示只能序列化，只能从db中读取该字段
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)  # required=False 表示反序列化时，可不传入该字段
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    logo = serializers.ImageField(label='图片', required=False)

    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 反向关联HeroInfo类，注意：heroinfo_set字段名为固定写法，因为heroinfo_set是BookInfo类中的一个属性值


class BookRelateField(serializers.RelatedField):
    """自定义外键字段"""

    def to_representation(self, value):
        return 'Book: %d %s' % (value.id, value.btitle)


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)  # choices 选择字段
    hcontent = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)  # allow_null=True 表示在序列化时，该字段允许为空，不然会报错

    # 外键处理
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)  # 在序列化时生效
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())  # 在反序列化时生效，由于反序列化时要进行参数校验、验证该字段是否合法

    # hbook = BookInfoSerializer()  # 嵌套图书序列化器类的字段

    hbook = BookRelateField(read_only=True)  # 由于继承了RelatedField类，所以要指定该字段在序列化或反序列化时的动作