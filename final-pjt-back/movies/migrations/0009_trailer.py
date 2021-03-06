# Generated by Django 3.2.12 on 2022-05-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailer_id', models.CharField(max_length=100)),
                ('movie_id', models.IntegerField()),
                ('iso_639_1', models.CharField(max_length=100)),
                ('iso_3166_1', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('official', models.CharField(max_length=100)),
                ('published_at', models.CharField(max_length=100)),
            ],
        ),
    ]
