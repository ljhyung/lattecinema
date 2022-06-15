from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from movies.serializers import ReviewSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    followings = UserSerializer(read_only=True, many=True)
    followers = UserSerializer(read_only=True, many=True)
    like_articles = ArticleSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many = True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles', 'last_name', 'first_name', 'followers', 'followings',)

