from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDeleteView,
    PublisherListView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView,
    ArtistListView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView,
    AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    MangaListView, MangaCreateView, MangaUpdateView, MangaDeleteView,
    MangaVolumeListView, MangaVolumeCreateView, MangaVolumeUpdateView, MangaVolumeDeleteView
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
    #Create, Update and Delete views
    path('language/create/', LanguageCreateView.as_view()),
    path('language/delete/<int:pk>/', LanguageDeleteView.as_view()),
    path('language/update/<int:pk>/', LanguageUpdateView.as_view()),
    path('publisher/create/', PublisherCreateView.as_view()),
    path('publisher/delete/<int:pk>/', PublisherDeleteView.as_view()),
    path('publisher/update/<int:pk>/', PublisherUpdateView.as_view()),
    path('artist/create/', ArtistCreateView.as_view()),
    path('artist/delete/<int:pk>/', ArtistDeleteView.as_view()),
    path('artist/update/<int:pk>/', ArtistUpdateView.as_view()),
    path('author/create/', AuthorCreateView.as_view()),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view()),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('manga/create/', MangaCreateView.as_view()),
    path('manga/delete/<int:pk>/', MangaDeleteView.as_view()),
    path('manga/update/<int:pk>/', MangaUpdateView.as_view()),
    path('manga-volume/create/', MangaVolumeCreateView.as_view()),
    path('manga-volume/delete/<int:pk>/', MangaVolumeDeleteView.as_view()),
    path('manga-volume/update/<int:pk>/', MangaVolumeUpdateView.as_view())
]
