from rest_framework.routers import DefaultRouter
from items import views


router = DefaultRouter()
router.register('', views.ItemViewSet, basename="item-viewset")

#
urlpatterns = router.urls
