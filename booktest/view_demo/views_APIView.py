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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.http import Http404


class BookListAPIView(APIView):
    """
    基础类视图：图书列表页
    """

    def get(self, request):
        """获取所有图书"""
        # 1、模型类交互
        try:
            queryset = BookInfo.objects.all()
        except BookInfo.DoesNotExist:
            return Response(data="您要访问的资源不存在", status=HTTP_404_NOT_FOUND)

        # 2、序列化数据
        serializer = BookInfoSerializer(queryset, many=True)
        # 3、响应数据
        return Response(data=serializer.data)

    def post(self, request):
        """新增图书"""
        # 1、反序列化数据
        serializer_class = BookInfoSerializer(data=request.data)

        # 2、数据校验
        serializer_class.is_valid(raise_exception=True)

        # 3、模型交互
        serializer_class.save()

        # 4、响应数据
        return Response(data=serializer_class.data, status=HTTP_201_CREATED)


class BookDetailAPIView(APIView):
    """
    基础类视图：图书详情页
    """

    def get(self, request, pk):
        # 1、模型类交互
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # return Response(data="您要访问的资源不存在!", status=HTTP_404_NOT_FOUND)
            raise Http404

        # 2、序列化数据
        serializer = BookInfoSerializer(book)

        # 3、响应数据
        return Response(data=serializer.data)

    def put(self, request, pk):
        """更新图书"""

        # 1、模型交互：获取对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # return Response(data="您要访问的资源不存在", status=HTTP_404_NOT_FOUND)
            raise Http404

        # 2、反序列化数据
        serializer = BookInfoSerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)

        # 3、数据更新
        serializer.save()

        # 4、响应数据
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, pk):
        """删除图书
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 抛出404
            raise Http404

        book.delete()

        return Response(status=HTTP_204_NO_CONTENT)
