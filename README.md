# DRF框架demo 

## 一、基础序列化器  
API: rest_framework.serializers.Serializer
### 1、模型构建、序列化器构建、序列化
- 模型构建：约束条件 blank、null、unique等字段的含义  
- 序列化器：  
    - 继承基础序列化器类：serializers  
    - 所有字段需手动定义  
    - 注意外键的关联写法：使用PrimaryKeyRelatedField 或 嵌套写法  
    - 约束条件：read_only=True、many=True、allow_null=True等字段的含义  

- 模型迁移时报错、回滚等操作  
- 序列化：从模型类 ==> 前端  

- 序列化测试环境：shell交互 或 视图类
    ```shell
    cd 项目根路径
    python manage.py shell
    ```  
    ```python
    >>> from booktest.models import BookInfo
    >>> from booktest.serializers import BookInfoSerializer
    
    >>> book = BookInfo.objects.get(id=2)
    >>> serializer = BookInfoSerializer(book)
    
    >>> serializer.data
    >>> # {'id': 2, 'btitle': '天龙八部', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None}
     ```       

### 2、反序列化
- 从前端 ==> 模型类

- 单个字段验证：validate_<field_name>
    ```python
    from rest_framework import serializers
  
    class BookInfoSerializer(serializers.Serializer):
        """图书数据序列化器"""
        ...
    
        def validate_btitle(self, value):
            if 'django' not in value.lower():
                raise serializers.ValidationError("图书不是关于Django的")
            return value
    ```

- 多个字段验证：validate
    ```python
    from rest_framework import serializers
  
    class BookInfoSerializer(serializers.Serializer):
        """图书数据序列化器"""
        ...
      
        def validate(self, attrs):
                bread = attrs['bread']
                bcomment = attrs['bcomment']
                if bread < bcomment:
                    raise serializers.ValidationError('阅读量小于评论量')
                return attrs
    ```


- 全局字段验证（针对任何序列化器-权限优先于 单个字段验证和多个字段验证）：validators
    ```python
    from rest_framework import serializers
  
    def about_drf(value):
        if 'DRF' not in value.uppper():
            raise serializers.ValidationError("图书不是关于DRF的")
    
    class BookInfoSerializer(serializers.Serializer):
        """图书数据序列化器"""
        id = serializers.IntegerField(label='ID', read_only=True)
        btitle = serializers.CharField(label='名称', max_length=20, validators=[about_drf])
        bpub_date = serializers.DateField(label='发布日期', required=False)
        bread = serializers.IntegerField(label='阅读量', required=False)
        bcomment = serializers.IntegerField(label='评论量', required=False)
        image = serializers.ImageField(label='图片', required=False)
    ```

- 反序列化测试环境：shell交互 或 视图类
    ```shell
    cd 项目根路径
    python manage.py shell
    ```
    ```python
    >>> from booktest.serializers import BookInfoSerializer
    
    >>> data = {"btitle": "hello wold"}
    >>> serializer = BookInfoSerializer(data=data)
    
    >>> # 1、验证字段是否合法
    >>> serializer.is_valid()  
    >>> # 2、查看错误信息
    >>> serializer.errors
    >>> # 3、获取验证通过后的数据
    >>> serializer.validated_data
  
    ```
    
-  新建数据
    ```python
    from rest_framework import serializers
    from booktest.models import BookInfo

    class BookInfoSerializer(serializers.Serializer):
        """图书数据序列化器"""
        ...
     
        def create(self, validated_data):
           """新建数据"""
            return BookInfo.objects.create(**validated_data)
    ```
    
    - 测试环境：shell交互 或 视图类
        ```shell
        cd 项目根路径
        python manage.py shell
        ```
        ```python
        >>> from booktest.serializers import BookInfoSerializer
        
        >>> data = {"btitle": "django_drf_test", "bread": 30, "bcomment": 20}
        >>> serializer = BookInfoSerializer(data=data)
        
        >>> serializer.is_valid()
        >>> serializer.save()
    
- 数据更新
    ```python
    from rest_framework import serializers

    class BookInfoSerializer(serializers.Serializer):
        """图书数据序列化器"""
        ...
      
        def update(self, instance, validated_data):
          """更新数据，instance为要更新的对象实例"""
            instance.btitle = validated_data.get('btitle', instance.btitle)
            instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
            instance.bread = validated_data.get('bread', instance.bread)
            instance.bcomment = validated_data.get('bcomment', instance.bcomment)
            instance.save()
            return instance
    ```
    - 测试环境：shell交互 或 视图类
        ```shell
        cd 项目根路径
        python manage.py shell
        ```
        ```python
        >>> from booktest.serializers import BookInfoSerializer
        >>> from booktest.models import BookInfo
        
        >>> book = BookInfo.objects.get(id=9)
        >>> data = {"btitle": "django_drf_test", "bread": 30, "bcomment": 20}
        >>> serializer = BookInfoSerializer(instance=book, data=data)
        
        >>> serializer.is_valid()
        >>> serializer.save()
        ```

- 新建数据 或 数据更新时，忽略序列化器约束条件：required=False
    - 数据更新案例
    - 测试环境：shell交互 或 视图类
        ```shell
        cd 项目根路径
        python manage.py shell
        ```
        ```python
        >>> from booktest.serializers import BookInfoSerializer
        >>> from booktest.models import BookInfo
        
        >>> book = BookInfo.objects.get(id=9)
        >>> data = {"bpub_date": date(2019, 3, 29), "bread": 80, "bcomment": 8}
        >>> serializer = BookInfoSerializer(instance=book, data=data, partial=True)
        
        >>> serializer.is_valid()
        >>> serializer.save()
        ```
        
