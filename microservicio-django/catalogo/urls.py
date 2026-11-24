from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, TrackViewSet

router = DefaultRouter()
router.register(r'albumes', AlbumViewSet, basename='album')
router.register(r'tracks', TrackViewSet, basename='track')

urlpatterns = router.urls
