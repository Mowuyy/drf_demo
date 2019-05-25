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
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class BookListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    扩展类视图：图书列表页
    """

    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    def get(self, request):
        """获取所有图书"""
        return self.list(request)

    def post(self, request):
        """新增图书"""
        return self.create(request)


class BookDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    扩展类视图：图书详情页
    """
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        """获取单一图书"""
        return self.retrieve(request)

    def put(self, request, pk):
        """更新图书"""
        return self.update(request)

    def delete(self, request, pk):
        """删除图书
        """
        return self.destroy(request)
