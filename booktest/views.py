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
from rest_framework.viewsets import ViewSet, ViewSetMixin, GenericViewSet, ModelViewSet
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import action


class BookInfoViewSet(ModelViewSet):
    """视图集扩展类视图"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # GET /books/latest/         detail=False 表示请求路径是复数资源
    # GET /books/{pk}/latest/    detail=True  表示请求路径是单一资源
    @action(methods=['GET'], detail=False)
    def latest(self, request):
        """查询最新图书"""
        try:
            book = BookInfo.objects.latest(field_name='id')
        except BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(instance=book)
        return Response(data=serializer.data)
