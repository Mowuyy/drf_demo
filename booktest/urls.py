from . import views
from rest_framework.routers import DefaultRouter
from booktest.views import BookInfoViewSet


# 支持额外扩展路由，在视图集中装饰器action指定路由
router = DefaultRouter()
router.register(r'books', BookInfoViewSet, base_name='book')

urlpatterns = []
urlpatterns += router.urls

for urls in urlpatterns:
    print(urls)
