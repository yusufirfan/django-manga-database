from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LanguageView, PublisherView, ArtistView, AuthorView, CategoryView, MangaView, MangaVolumeView

router = DefaultRouter()

router.register('language', LanguageView)
router.register('publisher', PublisherView)
router.register('artist', ArtistView)
router.register('author', AuthorView)
router.register('category', CategoryView)
router.register('manga', MangaView)
router.register('manga-volume', MangaVolumeView)

urlpatterns = [
    path('', include(router.urls)),
]
