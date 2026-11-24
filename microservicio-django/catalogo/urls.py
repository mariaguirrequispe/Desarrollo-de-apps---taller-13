from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, TrackViewSet
<<<<<<< HEAD
router = DefaultRouter()
router.register('albumes', AlbumViewSet)
router.register('tracks', TrackViewSet)
=======

router = DefaultRouter()
router.register(r'albumes', AlbumViewSet, basename='album')
router.register(r'tracks', TrackViewSet, basename='track')

>>>>>>> origin/main
urlpatterns = router.urls
