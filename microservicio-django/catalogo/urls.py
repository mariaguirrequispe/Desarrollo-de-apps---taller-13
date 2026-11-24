from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, TrackViewSet


router = DefaultRouter()
router.register('albumes', AlbumViewSet)
router.register('tracks', TrackViewSet)
urlpatterns = router.urls
