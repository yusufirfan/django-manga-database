from typing import Any, Dict, Iterable, Optional, Tuple
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

    def __str__(self):
        return self.name

class Publisher(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()
    website = models.CharField(max_length=35)
    logo = models.ImageField(upload_to='manga/publisher/')

    def __str__(self):
        return self.name

class Artist(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(FixModel):
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(FixModel):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class Manga(FixModel):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    original_name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='local_name')
    original_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='original_name')
    # volume = models.PositiveSmallIntegerField(null=True, blank=True)
    # total_volume = models.PositiveSmallIntegerField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    purchase_link = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.original_name}'

    # def get_volume_count_for_language(self, language):
    #     return MangaVolume.objects.filter(manga=self, language=language).count()

class MangaVolume(FixModel):
    manga = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    vol_num = models.PositiveSmallIntegerField()
    vol_name = models.CharField(max_length=35)
    cover = models.ImageField(upload_to='manga/covers/')

    def __str__(self):
        return f'[{self.language}] {self.manga} - {self.vol_num} - {self.vol_name}'

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         manga = Manga.objects.get(id=self.manga_id)

    #         if self.language == manga.original_language:
    #             manga.total_volume+=1
    #         elif self.language == manga.language:
    #             manga.volume+=1

    #         manga.save()
    #     return super().save(*args, **kwargs)