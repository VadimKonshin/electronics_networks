from rest_framework import generics

from store.models import NetworkEntity
from store.serializers import NetworkEntitySerializers


class NetworkEntityCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkEntitySerializers


class NetworkEntityListAPIView(generics.ListAPIView):
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()


class NetworkEntityRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()


class NetworkEntityUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()


class NetworkEntityDestroyAPIView(generics.DestroyAPIView):
    queryset = NetworkEntity.objects.all()
