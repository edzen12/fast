from rest_framework.routers import DefaultRouter

from .views import LinkPriceViewSet


router = DefaultRouter()
router.register(r'', LinkPriceViewSet, basename="linkprice")
urlpatterns = router.urls