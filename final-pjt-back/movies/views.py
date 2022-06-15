# articles/views.py
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count
from django.db.models import Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.models import User
from .models import Crew, Genre, Movie, Review
from .serializers import CrewSerializer, MovieSerializer, ReviewSerializer
from .serializers import GenreSerializer
from movies import serializers


@api_view(['GET', 'POST'])
def movie_list(request):

    def movie_list():
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    

    if request.method == 'GET':
        return movie_list()

@api_view(['GET'])
def genre_movie_list(request, genre_pk):
    movies = Movie.objects.all()
    genre = Genre.objects.filter(pk=12)
    # print(genre)
    random_genre = random.choices(genre, k=4)
    serializer = GenreSerializer(random_genre, many=True)
    # print(serializer.data)
    movie_id = Movie.objects.filter(genres__pk=genre_pk)
    # print(movie_id)
    # movies = Movie.objects.filter(id=Movie.genres)

    serializer = MovieSerializer(movie_id, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def search_movie_list(request, keyword):
    print(keyword)
    movies = Movie.objects.filter(title__icontains=keyword)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.filter(pk=movie_pk)
    print(movie)
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_rate(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rate = movie.movie_reviews.all().aggregate(Avg('rate'))
    rate_json = {'rate': rate}
    return JsonResponse(rate_json, safe=False)


@api_view(['GET'])
def movie_crew_detail(request, movie_pk):
    crew = Crew.objects.filter(pk=movie_pk)
    # print(crew)
    serializer = CrewSerializer(crew, many=True)
    # print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def create_reviews(request, movie_pk):
    user = request.user
    # print(request)
    movie = get_object_or_404(Movie, pk=movie_pk)
    # print(request.data)
    serializer = ReviewSerializer(data=request.data)
    # print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        reviews = movie.movie_reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.movie_reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.movie_reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # print(review)
    # print(review.liked_Movie_review)
    # print(review.user_review_liked)
    if review.user_review_liked.filter(pk=request.user.pk).exists():
        review.user_review_liked.remove(request.user)
    else:
        review.user_review_liked.add(request.user)
    review_liked = review.user_review_liked.filter(pk=request.user.pk).exists()
    # review_liked_num = review.user_review_liked.count()
    data = {
        'review_liked': review_liked,
        # 'review_liked_num': review_liked_num,
    }
    return JsonResponse(data)

    
@api_view(['GET'])
def genre_name(request, genre_pk):
    genre = Genre.objects.filter(pk=genre_pk)
    # print(crew)
    serializer = GenreSerializer(genre, many=True)
    # print(serializer.data)
    return Response(serializer.data)