from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    '''вьюсет для юзеров'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
