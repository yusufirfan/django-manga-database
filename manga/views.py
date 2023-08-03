from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import (Language, LanguageSerializer, 
                          Publisher, PublisherSerializer, 
                          Artist, ArtistSerializer, 
                          Author, AuthorSerializer, 
                          Category, CategorySerializer, 
                          Manga, MangaSerializer, 
                          MangaVolume, MangaVolumeSerializer)

class FixView(ModelViewSet):
    pass

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
    
#Language Views
class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminOrReadOnly]

class LanguageCreateView(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]

class LanguageUpdateView(UpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]

class LanguageDeleteView(DestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]

# Publisher Views
class PublisherListView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminOrReadOnly]

class PublisherCreateView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]

class PublisherUpdateView(UpdateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]

class PublisherDeleteView(DestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]

# Artist Views
class ArtistListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]

class ArtistCreateView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminUser]

class ArtistUpdateView(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminUser]

class ArtistDeleteView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminUser]

# Author Views
class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class AuthorDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

# Category Views
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

# Manga Views
class MangaListView(ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAdminOrReadOnly]

class MangaCreateView(CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAdminUser]

class MangaUpdateView(UpdateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAdminUser]

class MangaDeleteView(DestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAdminUser]

# MangaVolume Views
class MangaVolumeListView(ListAPIView):
    queryset = MangaVolume.objects.all()
    serializer_class = MangaVolumeSerializer
    permission_classes = [IsAdminOrReadOnly]

class MangaVolumeCreateView(CreateAPIView):
    queryset = MangaVolume.objects.all()
    serializer_class = MangaVolumeSerializer
    permission_classes = [IsAdminUser]

class MangaVolumeUpdateView(UpdateAPIView):
    queryset = MangaVolume.objects.all()
    serializer_class = MangaVolumeSerializer
    permission_classes = [IsAdminUser]

class MangaVolumeDeleteView(DestroyAPIView):
    queryset = MangaVolume.objects.all()
    serializer_class = MangaVolumeSerializer
    permission_classes = [IsAdminUser]