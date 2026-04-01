from rest_framework.routers import DefaultRouter
from .views import TourViewSet, GalleryImageViewSet

router = DefaultRouter()
router.register('tours', TourViewSet)
router.register('gallery', GalleryImageViewSet)

urlpatterns = router.urls