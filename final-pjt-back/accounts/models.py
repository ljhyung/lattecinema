from django.db import models
from django.contrib.auth.models import AbstractUser
from articles.models import Comment
from movies.models import Review


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    liked_Movie_review = models.ManyToManyField(Review, related_name="user_review_liked")
    liked_comment = models.ManyToManyField(Comment, related_name="user_liked")

