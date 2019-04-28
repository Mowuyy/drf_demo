1、DRF框架demo -- 模型构建、序列化器构建

2、模型构建：约束条件 blank、null、unique等字段的含义

3、序列化器：
    1）继承基础序列化器类：serializers
    2）所有字段需手动定义
    3）注意外键的关联写法：使用PrimaryKeyRelatedField 或 嵌套写法
    4）约束条件：read_only=True、many=True、allow_null=True等字段的含义

4、模型迁移时报错、回滚等操作

5、序列化：从模型类 ==> 前端

6、测试环境：
        python manage.py shell

        from booktest.models import BookInfo
        from booktest.serializers import BookInfoSerializer

        book = BookInfo.objects.get(id=2)
        serializer = BookInfoSerializer(book)

        serializer.data
        # {'id': 2, 'btitle': '天龙八部', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None}

