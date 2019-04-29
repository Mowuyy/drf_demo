from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers_base import BookInfoSerializer
from .models import BookInfo


class BookInfoViewSet(ModelViewSet):
    """
    restful风格的url:
        GET => http://127.0.0.1:8000/books/

        POST => http://127.0.0.1:8000/books/
                body: json数据传参

        PUT => http://127.0.0.1:8000/books/8/
               body: json数据传参

        DELETE => http://127.0.0.1:8000/books/8/
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
