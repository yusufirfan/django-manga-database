from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LanguageListView, LanguageCreateView, LanguageDeleteView,
    PublisherListView, PublisherCreateView, PublisherDeleteView,
    ArtistListView, ArtistCreateView, ArtistDeleteView,
    AuthorListView, AuthorCreateView, AuthorDeleteView,
    CategoryListView, CategoryCreateView, CategoryDeleteView,
    MangaListView, MangaCreateView, MangaDeleteView,
    MangaVolumeListView, MangaVolumeCreateView, MangaVolumeDeleteView
)

router = DefaultRouter()

urlpatterns = [
    path('language/', LanguageListView.as_view()),
    path('publisher/', PublisherListView.as_view()),
    path('artist/', ArtistListView.as_view()),
    path('author/', AuthorListView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('manga/', MangaListView.as_view()),
    path('manga-volume/', MangaVolumeListView.as_view()),
    #Create and Delete views
    path('language/create/', LanguageCreateView.as_view()),
    path('language/delete/<int:pk>/', LanguageDeleteView.as_view()),
    path('publisher/create/', PublisherCreateView.as_view()),
    path('publisher/delete/<int:pk>/', PublisherDeleteView.as_view()),
    path('artist/create/', ArtistCreateView.as_view()),
    path('artist/delete/<int:pk>/', ArtistDeleteView.as_view()),
    path('author/create/', AuthorCreateView.as_view()),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('manga/create/', MangaCreateView.as_view()),
    path('manga/delete/<int:pk>/', MangaDeleteView.as_view()),
    path('manga-volume/create/', MangaVolumeCreateView.as_view()),
    path('manga-volume/delete/<int:pk>/', MangaVolumeDeleteView.as_view())
]
