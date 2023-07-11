from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Anime(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    aired = models.CharField(max_length=255, blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    ranked = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Manga(models.Model):
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=20)
    imgPath = models.CharField(max_length=255)
    genre = models.TextField()
    alternativeTitle = models.TextField()
    staff = models.TextField()

    def __str__(self):
        return self.title


class ReviewAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class ReviewManga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class FavoriteAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.anime.title}"


class FavoriteManga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.manga.title}"


class Discussion(models.Model):
    TAGE_CHOICES = (
        ('anime', 'Anime'),
        ('manga', 'Manga'),
        ('characters', 'Characters'),
        ('games', 'Games'),
        ('general', 'General'),
    )
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, choices=TAGE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
