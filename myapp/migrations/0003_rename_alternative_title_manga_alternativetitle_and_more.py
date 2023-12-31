# Generated by Django 4.1.9 on 2023-07-06 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_manga_rename_english_name_anime_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='alternative_title',
            new_name='alternativeTitle',
        ),
        migrations.CreateModel(
            name='ReviewAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
