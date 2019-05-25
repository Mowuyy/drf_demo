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
urlpatterns = [
    url(r'^books/$', BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
"""


from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
from rest_framework.viewsets import ViewSet, ViewSetMixin
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# class BookInfoViewSet(ViewSetMixin, APIView):
class BookInfoViewSet(ViewSet):
    """视图集基础类视图"""
    # GET /books/
    def list(self, request):
        """获取所有图书"""
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)

        return Response(data=serializer.data)

    # /books/(?P<pk>\d+)/
    def retrieve(self,request, pk=None):
        """获取单一图书"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(instance=book)
        return Response(data=serializer.data)

    # POST /books/
    def create(self, request):
        """创建图书"""
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    # PUT /books/(?P<pk>\d+)/
    def update(self, reqeust, pk=None):
        """更新图书"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(instance=book, data=reqeust.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

    # DELETE /books/(?P<pk>\d+)/
    def destroy(self, request, pk=None):
        """删除图书"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

