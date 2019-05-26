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
    
- 新建数据
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
        ```

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
        
## 二、高级序列化器  
作用：DRF自动创建
API: rest_framework.serializers.ModelSerializer

### 1、定义所有字段：fields = '\__all__'

- 测试案例
    ```python
    from rest_framework import serializers
    from .models import BookInfo
            
    class BookInfoSerializer(serializers.ModelSerializer):
        """图书数据序列化器"""
        class Meta:
            model = BookInfo
            fields = '__all__'
    ```
- 序列化测试环境：shell交互 或 视图类
    ```shell
    cd 项目根路径
    python manage.py shell
    ```
    
    ```python
    >>> from booktest.models import BookInfo
    >>> from booktest.serializers import BookInfoSerializer
    
    >>> book = BookInfo.objects.get(id=6)
    >>> serializer = BookInfoSerializer(book)
    >>> serializer.data
    ```
- 反序列化测试环境：shell交互 或 视图类
    ```shell
    cd 项目根路径
    python manage.py shell
    ```
    
    ```python
    >>> from booktest.models import BookInfo
    >>> from booktest.serializers import BookInfoSerializer
    
    >>> data = {"btitle": "极限挑战"}
    >>> serializer = BookInfoSerializer(data=data)
    >>> serializer.is_valid()
    >>> serializer.save()
    ```
    
### 2、定义指定字段：fields = ()
- 指定需要字段
    ```python
    from rest_framework import serializers
    from .models import BookInfo
            
    class BookInfoSerializer(serializers.ModelSerializer):
        """图书数据序列化器"""
        class Meta:
            model = BookInfo
            fields = ('id', 'btitle', 'bpub_date')
    ```
- 指定不需要字段
    ```python
    from rest_framework import serializers
    from .models import BookInfo
            
    class BookInfoSerializer(serializers.ModelSerializer):
        """图书数据序列化器"""
        class Meta:
            model = BookInfo
            exclude = ('logo',)
    ```
- 外键
    - 主键关联
        ```python
        from rest_framework import serializers
        from .models import HeroInfo
        
        class HeroInfoSerializer(serializers.ModelSerializer):
            class Meta:
                model = HeroInfo
                fields = ('id', 'hname', 'hgender', 'hcontent', 'hbook')  # hbook为主键外键
        ```
    - 嵌套关联
        ```python
        from rest_framework import serializers
        from .models import HeroInfo
        
        class HeroInfoSerializer(serializers.ModelSerializer):
            """英雄数据序列化器"""
            class Meta:
                model = HeroInfo
                fields = '__all__'
                depth = 1  # 1层嵌套外键
        ```
    - 嵌套关联（自定义处理）
        ```python
        from rest_framework import serializers
        from .models import HeroInfo, BookInfo
          
        class BookInfoSerializer(serializers.ModelSerializer):
            """图书数据序列化器"""
        
            class Meta:
                model = BookInfo
                fields = '__all__'
        ```

        ```python
        class HeroInfoSerializer(serializers.ModelSerializer):
            """英雄数据序列化器"""
      
            hbook = BookInfoSerializer(many=True)  # 自定义嵌套外键
        
            class Meta:
                model = HeroInfo
                fields = ('id', 'hname', 'hgender', 'hcontent', 'hbook')
        ```
### 3、约束条件：read_only_fields、extra_kwargs
- 指定只读约束：read_only_fields
    ```python
    from rest_framework import serializers
    from .models import BookInfo
    
    class BookInfoSerializer(serializers.ModelSerializer):
        """图书数据序列化器"""
    
        class Meta:
            model = BookInfo
            fields = '__all__'
          
            read_only_fields = ('id', 'bread', 'bcomment')
    ```
- 指定其他约束：extra_kwargs
    ```python
    from rest_framework import serializers
    from .models import BookInfo
    
    class BookInfoSerializer(serializers.ModelSerializer):
        """图书数据序列化器"""
    
        class Meta:
            model = BookInfo
            fields = '__all__'
          
            extra_kwargs = {
                    'bread': {'min_value': 0, 'required': True},
                    'bcomment': {'min_value': 0, 'required': True},
            }
    ```

## 三、基础类视图
### 1、APIView、GenericAPIView
- APIView：不与数据库交互时使用该类视图
    - 案例1：列表页查询  
        ```python
        class BookListAPIView(APIView):
        """
        图书列表页
        """

        def get(self, request):
            # 1、模型类交互
            try:
                queryset = BookInfo.objects.all()
            except BookInfo.DoesNotExist:
                return Response(data="您要访问的资源不存在", status=HTTP_404_NOT_FOUND)

            # 2、序列化数据
            serializer = BookInfoSerializer(queryset, many=True)
            # 3、响应数据
            return Response(data=serializer.data)
        ```
        
    - 案例2：详情页查询
        ```python
        class BookDetailAPIView(APIView):
        """
        图书详情页
        """

        def get(self, request, pk):
            # 1、模型类交互
            try:
                book = BookInfo.objects.get(pk=pk)
            except BookInfo.DoesNotExist:
                return Response(data="您要访问的资源不存在!", status=HTTP_404_NOT_FOUND)

            # 2、序列化数据
            serializer = BookInfoSerializer(book)
            # 3、响应数据
            return Response(data=serializer.data)
        ```

- GenericAPIView：与数据库交互时使用类视图

      

### 2、扩展类：ListModelMixin、CreateModelMixin、RetrieveModelMixin、UpdateModelMixin、DestroyModelMixin
