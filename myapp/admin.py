from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Anime, Manga, ReviewAnime, ReviewManga, FavoriteAnime, FavoriteManga, Discussion, Comment



admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(ReviewManga)
admin.site.register(ReviewAnime)
admin.site.register(FavoriteAnime)
admin.site.register(FavoriteManga)
admin.site.register(Discussion)
admin.site.register(Comment)




