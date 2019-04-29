from rest_framework import serializers
from .models import BookInfo

"""
序列化器字段说明 => https://www.django-rest-framework.org/api-guide/fields/

基础序列化器使用如下：

"""


def about_drf(value):
    if 'DRF' not in value.upper():
        raise serializers.ValidationError("图书不是关于DRF的")


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器
       继承Serializer类
    """
    id = serializers.IntegerField(label='ID', read_only=True)  # read_only=True 表示只能序列化，只能从db中读取该字段（一般主键设置参数read_only=True）
    btitle = serializers.CharField(label='名称', max_length=20, validators=[about_drf])
    bpub_date = serializers.DateField(label='发布日期', required=False)  # required=False 表示反序列化时，可不传入该字段
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    logo = serializers.ImageField(label='图片', required=False)

    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 反向关联HeroInfo类，注意：heroinfo_set字段名为固定写法，因为heroinfo_set是BookInfo类中的一个属性值

    def validate_btitle(self, value):
        """单个字段验证"""
        if 'django' not in value.lower():
            raise serializers.ValidationError("图书不是关于Django的")
        return value

    def validate(self, attrs):
        """多个字段验证"""
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    def create(self, validated_data):
        """新建数据"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新数据，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance


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

    hbook = BookInfoSerializer()  # 嵌套图书序列化器类的字段，

    # hbook = BookRelateField(read_only=True)  # 由于继承了RelatedField类，所以要指定该字段在序列化或反序列化时的动作
