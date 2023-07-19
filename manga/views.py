from rest_framework.viewsets import ModelViewSet

class FixView(ModelViewSet):
    pass

from .serializers import (Language, LanguageSerializer, 
                          Publisher, PublisherSerializer, 
                          Artist, ArtistSerializer, 
                          Author, AuthorSerializer, 
                          Category, CategorySerializer, 
                          Manga, MangaSerializer, 
                          MangaVolume, MangaVolumeSerializer)

class LanguageView(FixView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class PublisherView(FixView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ArtistView(FixView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AuthorView(FixView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryView(FixView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MangaView(FixView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class MangaVolumeView(FixView):
    queryset = MangaVolume.objects.all()
    serializer_class = MangaVolumeSerializer