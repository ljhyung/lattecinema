from movies.models import Movie, Genre, Crew, Review, trailers
from rest_framework import serializers
from django.contrib.auth import get_user_model

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name',)

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    user_review_liked = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'title', 'content', 'rate', 'created_at', 'updated_at', 'movie', 'user_review_liked')
        read_only_fields = ('movie', )


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = trailers
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    movie_reviews = ReviewSerializer(read_only=True, many=True)
    trailer = TrailerSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'



