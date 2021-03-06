# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-27 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(default=0, verbose_name='评论量'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, verbose_name='图书名称'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='logo',
            field=models.CharField(default='测试', max_length=50, verbose_name='主图片'),
        ),
        migrations.AlterModelTable(
            name='heroinfo',
            table='heroinfo',
        ),
    ]
