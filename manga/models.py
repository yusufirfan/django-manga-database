from django.db import models
from django.contrib.auth.models import User

class FixModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
    
class Language(FixModel):
    name = models.CharField(max_length=25)

class Publisher(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()
    website = models.CharField(max_length=35)
    logo = models.ImageField(upload_to='manga/publisher/')

class Artist(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()

class Author(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()

class Category(FixModel):
    name = models.CharField(max_length=75)

class Manga(FixModel):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    original_name = models.CharField(max_length=255)
    volume = models.PositiveSmallIntegerField()
    total_volume = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    purchase_link = models.URLField()

class MangaVolume(FixModel):
    manga = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    vol_num = models.PositiveSmallIntegerField()
    vol_name = models.CharField(max_length=35)
    cover = models.ImageField(upload_to='manga/covers/')