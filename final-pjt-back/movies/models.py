from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    # G = models.IntegerField()
    name = models.CharField(max_length=50)
    
class Movie(models.Model):
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=500, null=True)
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    original_language = models.CharField(max_length=150, null=True)
    original_title = models.CharField(max_length=150, null=True)
    overview = models.CharField(max_length=1000, null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(max_length=500, null=True)
    release_date = models.DateField(null=True)
    runtime = models.IntegerField(null=True)
    tagline = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=150, null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)


class Crew(models.Model):
    Director = models.CharField(max_length=1000)
    Actor = models.TextField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_reviews")
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class trailers(models.Model):
    movie_id = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name="trailer")
    trailer_id = models.CharField(max_length=100)
    # movie_id = models.IntegerField()
    iso_639_1 = models.CharField(max_length=100)
    iso_3166_1 = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    size = models.IntegerField()
    type = models.CharField(max_length=100)
    official = models.CharField(max_length=100)
    published_at = models.CharField(max_length=100)



    