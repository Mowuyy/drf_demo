from django.db import models


# Create your models here.


class BookInfo(models.Model):
    """定义图书模型类BookInfo"""
    btitle = models.CharField(max_length=20, blank=True, verbose_name="图书名称")  # blank=True 表示该字段表单传参时，允许包含空白字符
    bpub_date = models.DateField(null=True, verbose_name="发布日期")  # null=True 表示该字段允许为空
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    logo = models.CharField(max_length=50, default='测试', verbose_name="主图片")
    isDelete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:  # 元类，表示对该模型类的约束条件
        db_table = 'bookInfo'  # 指定表的名称

    def __str__(self):
        """输出该类对象时要显示的内容"""
        return self.btitle


class HeroInfo(models.Model):
    """定义英雄模型类HeroInfo"""
    hname = models.CharField(max_length=20, unique=True, verbose_name="英雄姓名")  # unique=True 表示该字段为唯一值
    hgender = models.BooleanField(default=True, verbose_name="英雄性别")
    isDelete = models.BooleanField(default=False, verbose_name="逻辑删除")
    hcontent = models.CharField(max_length=100, verbose_name="英雄描述信息")
    hbook = models.ForeignKey('BookInfo', verbose_name="一对多关联图书表")

    class Meta:
        db_table = "heroInfo"

    def __str__(self):
        return self.hname
