from rest_framework.routers import DefaultRouter

from .views import SocialViewSet, ReviewsViewSet


router = DefaultRouter()
router.register(r'social', SocialViewSet, basename="social")
router.register(r'reviews', ReviewsViewSet, basename="reviews")
urlpatterns = router.urls