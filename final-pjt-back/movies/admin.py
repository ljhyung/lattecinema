import imp
from django.contrib import admin
from .models import Movie, Genre, Crew,Review


# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Crew)
admin.site.register(Review)