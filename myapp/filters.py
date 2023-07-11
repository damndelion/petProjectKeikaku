import django_filters

from .models import Anime, Manga


class AnimeFilter(django_filters.FilterSet):
    CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Cars', 'Cars'),
        ('Comedy', 'Comedy'),
        ('Demons', 'Demons'),
        ('Drama', 'Drama'),
        ('Ecchi', 'Ecchi'),
        ('Fantasy', 'Fantasy'),
        ('Game', 'Game'),
        ('Harem', 'Harem'),
        ('Hentai', 'Hentai'),
        ('Historical', 'Historical'),
        ('Horror', 'Horror'),
        ('Josei', 'Josei'),
        ('Kids', 'Kids'),
        ('Magic', 'Magic'),
        ('Martial Arts', 'Martial Arts'),
        ('Mecha', 'Mecha'),
        ('Military', 'Military'),
        ('Mystery', 'Mystery'),
        ('Parody', 'Parody'),
        ('Police', 'Police'),
        ('Psychological', 'Psychological'),
        ('Romance', 'Romance'),
        ('Samurai', 'Samurai'),
        ('School', 'School'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Seinen', 'Seinen'),
        ('Shoujo', 'Shoujo'),
        ('Shounen', 'Shounen'),
        ('Slice of life', 'Slice of life'),
        ('Space', 'Space'),
        ('Sports', 'Sports'),
        ('Super Power', 'Super Power'),
        ('Supernatural', 'Supernatural'),
        ('Thriller', 'Thriller'),
        ('Vampire', 'Vampire')
    )

    genre = django_filters.ChoiceFilter(label='Genre', choices=CHOICES, lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('popularity', 'popularity'),
            ('ranked', 'ranked'),
            ('score', 'score'),
        )
    )

    class Meta:
        model = Anime
        fields = ['genre']


class MangaFilter(django_filters.FilterSet):
    CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Magic', 'Magic'),
        ('Mystery', 'Mystery'),
        ('Psychological', 'Psychological'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Slice of life', 'Slice of life'),
        ('Supernatural', 'Supernatural'),
        ('Thriller', 'Thriller'),
        ('Tournament', 'Tournament'),
    )

    ordering = django_filters.OrderingFilter(
        fields=('rating', 'rating')
    )

    genre = django_filters.ChoiceFilter(label='Genre', choices=CHOICES, lookup_expr='icontains')

    class Meta:
        model = Manga
        fields = ['genre']