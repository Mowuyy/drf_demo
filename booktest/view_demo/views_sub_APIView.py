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
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView


# class BookListAPIView(ListAPIView, CreateAPIView):
class BookListAPIView(ListCreateAPIView):
    """
    子类视图：图书列表页
    """
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()


# class BookDetailAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    子类视图：图书详情页
    """
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()
