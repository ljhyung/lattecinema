from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('movies/search/<str:keyword>/', views.search_movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/rate/', views.user_rate),
    path('movies/genre/<int:genre_pk>/', views.genre_movie_list),
    path('movies/genre/<int:genre_pk>/name/', views.genre_name),
    path('movies/<int:movie_pk>/crew/', views.movie_crew_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_reviews),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    path('movies/reviews/<int:review_pk>/', views.review_like),
]