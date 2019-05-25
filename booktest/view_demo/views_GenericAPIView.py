from django.shortcuts import render

# Create your views here.


# from rest_framework.viewsets import ModelViewSet
# from .serializers_base import BookInfoSerializer
# from .models import BookInfo


# class BookInfoViewSet(ModelViewSet):
#     """
#     restful风格的url:
#         GET => http://127.0.0.1:8000/books/
#
#         POST => http://127.0.0.1:8000/books/
#                 body: json数据传参
#
#         PUT => http://127.0.0.1:8000/books/8/
#                body: json数据传参
#
#         DELETE => http://127.0.0.1:8000/books/8/
#     """
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer

"""
from django.conf.urls import url
from .views import BookListAPIView, BookDetailAPIView


urlpatterns = [
    url(r'^books/$', BookListAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookDetailAPIView.as_view()),
]
"""


from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK


class BookListAPIView(GenericAPIView):
    """
    一般类视图：图书列表页
    """

    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    def get(self, request):
        """获取所有图书"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request):
        """新增图书"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=HTTP_201_CREATED)


class BookDetailAPIView(GenericAPIView):
    """
    一般类视图：图书详情页
    """
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        """获取单一图书"""
        # 1、获取对象
        book = self.get_object()
        # 2、序列化数据
        serializer = self.get_serializer(instance=book)
        # 3、响应数据
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        """更新图书"""
        # 1、获取单一对象
        book = self.get_object()
        # 2、序列化数据
        serializer = self.get_serializer(instance=book, data=request.data)
        # 3、数据校验
        serializer.is_valid()
        # 4、模型交互：数据保存
        serializer.save()
        # 5、响应数据
        return Response(data=serializer.data)

    def delete(self, request, pk):
        """删除图书
        """
        book = self.get_object()
        book.delete()

        return Response(status=HTTP_204_NO_CONTENT)
