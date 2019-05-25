# 设置Django运行所依赖环境变量
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_demo.settings")

# 让Django环境进行一次初始化
import django

django.setup()

import json

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer

# 需求：
# 1. 进行数据校验时，btitle的内容必须包含`django`
# 2. 进行数据校验时，bread必须大于等于bcomment

if __name__ == "__main__":
    # 获取id为1的图书
    book = BookInfo.objects.get(id=1)

    # 准备数据
    data = {'btitle': '射雕英雄传-2', 'bpub_date': '2000-01-01'}

    # 创建序列化器对象
    serializer = BookInfoSerializer(book, data=data)

    # 反序列化-数据校验
    res = serializer.is_valid()
    print(res)

    # 反序列化-数据保存(调用序列化器类中update)
    serializer.save()

    # 获取更新对象序列化之后的数据
    print(serializer.data)

# if __name__ == "__main__":
#     # 准备数据
#     data = {'btitle': 'python', 'bpub_date': '2019-05-21', 'bread': 21, 'bcomment': 20}
#     # data = {'btitle': 'python', 'bpub_date': 'abc'}
#
#     # 创建序列化器类对象
#     serializer = BookInfoSerializer(data=data)
#
#     # 反序列化-数据校验
#     res = serializer.is_valid()
#     print(res)
#
#     # 如果失败，获取出错信息
#     # print(serializer.errors)
#
#     # 如果成功，获取校验之后的数据
#     # print(serializer.validated_data)
#
#     # 反序列化-数据保存(调用序列器类中create方法)
#     serializer.save()
#
#     # 获取新增对象序列化之后的数据
#     print(serializer.data)


# if __name__ == "__main__":
#     # 序列化单个对象
#     book = BookInfo.objects.get(id=1)
#
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(book)
#
#     # 获取序列化之后的数据
#     res = serializer.data
#
#     # 格式化显示数据
#     res = json.dumps(res, indent=1, ensure_ascii=False)
#     print(res)


# if __name__ == "__main__":
#     # 获取id为1的英雄
#     hero = HeroInfo.objects.get(id=1)
#
#     # 创建序列化器对象
#     serializer = HeroInfoSerializer(hero)
#
#     # 获取序列化之后的数据
#     res = serializer.data
#
#     # 格式化显示数据
#     res = json.dumps(res, indent=1, ensure_ascii=False)
#     print(res)

# if __name__ == "__main__":
#     # 序列化多个对象
#     books = BookInfo.objects.all() # QuerySet
#
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(books, many=True)
#
#     # 获取序列化之后的数据
#     res = serializer.data
#
#     # 格式化显示数据
#     res = json.dumps(res, indent=1, ensure_ascii=False)
#     print(res)

# if __name__ == "__main__":
#     # 序列化单个对象
#     book = BookInfo.objects.get(id=1)
#
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(book)
#
#     # 获取序列化之后的数据
#     print(serializer.data)
