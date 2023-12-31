# Generated by Django 4.1.9 on 2023-06-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=20)),
                ('imgPath', models.CharField(max_length=255)),
                ('genre', models.TextField()),
                ('alternative_title', models.TextField()),
                ('staff', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='English_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Aired',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Duration',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Episodes',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Genres',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Japanese_name',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Licensors',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Popularity',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Premiered',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Producers',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Ranked',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Rating',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Score',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Source',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Studios',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='Type',
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='synopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='anime',
            name='aired',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='popularity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='ranked',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
