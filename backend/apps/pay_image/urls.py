from rest_framework.routers import DefaultRouter

from .views import PayImageViewSet


router = DefaultRouter()
router.register(r'', PayImageViewSet, basename="pay_image")
urlpatterns = router.urls