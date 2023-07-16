from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Artist)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Manga)
admin.site.register(MangaVolume)