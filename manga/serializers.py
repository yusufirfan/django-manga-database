from rest_framework import serializers

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)
    
from .models import (Language, 
                     Publisher, 
                     Artist, 
                     Author, 
                     Category,
                     Manga, 
                     MangaVolume)

class LanguageSerializer(FixSerializer):
    language_total = serializers.SerializerMethodField()

    def get_language_total(self, obj):
        return Language.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Language
        exclude = []

class PublisherSerializer(FixSerializer):
    publisher_total = serializers.SerializerMethodField()

    def get_publisher_total(self, obj):
        return Publisher.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Publisher
        exclude = []

class ArtistSerializer(FixSerializer):
    artist_total = serializers.SerializerMethodField()

    def get_artist_total(self, obj):
        return Artist.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Artist
        exclude = []

class AuthorSerializer(FixSerializer):
    author_total = serializers.SerializerMethodField()

    def get_author_total(self, obj):
        return Author.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Author
        exclude = []

class CategorySerializer(FixSerializer):
    category_total = serializers.SerializerMethodField()

    def get_category_total(self, obj):
        return Category.objects.filter(id=obj.id).count()
    
    class Meta:
        model = Category
        exclude = []

class MangaSerializer(FixSerializer):
    language = serializers.StringRelatedField()
    original_language = serializers.StringRelatedField()
    local_volume = serializers.SerializerMethodField()
    total_volume = serializers.SerializerMethodField()
    publisher = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    artist = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    
    def get_local_volume(self, obj):
        return MangaVolume.objects.filter(manga=obj, language=obj.language).count()
    
    def get_total_volume(self, obj):
        return MangaVolume.objects.filter(manga=obj, language=obj.original_language).count()

    class Meta:
        model = Manga
        exclude = []

class MangaVolumeSerializer(FixSerializer):

    class Meta:
        model = MangaVolume
        exclude = []