from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def get_user_by_username(username):
    return get_object_or_404(User, username=username)


def user_authenticated(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    return user
