from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET','PUT'])
def profile(request, username):
    if request.method == 'GET':
        user = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        user = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    

@api_view(['POST'])
def follow(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    print(person)
    print(person.followers)
    print(person.followings)
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    followerNum = person.followers.count()
    followed = person.followers.filter(pk=request.user.pk).exists()
    data = {
        'profile_username': person.username,
        'followerNum': followerNum,
        'followed': followed,
    }
    return JsonResponse(data)


# @api_view(['PUT'])
# def update_article(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = ProfileSerializer(instance=user, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)