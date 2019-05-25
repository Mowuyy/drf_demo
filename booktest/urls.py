from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url
from booktest.views import BookInfoViewSet


router = DefaultRouter()
router.register(r'books', BookInfoViewSet, base_name='book')

urlpatterns = []
urlpatterns += router.urls

for urls in urlpatterns:
    print(urls)
