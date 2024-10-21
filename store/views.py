from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from store.models import NetworkEntity, Product
from store.permissions import IsActiveUserPermissions
from store.serializers import NetworkEntitySerializers, ProductSerializers


class NetworkEntityCreateAPIView(generics.CreateAPIView):
    '''Класс создания сети'''
    serializer_class = NetworkEntitySerializers
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityListAPIView(generics.ListAPIView):
    ''' Класс просмотра магазинов '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)
    permission_classes = [IsActiveUserPermissions]



class NetworkEntityRetrieveAPIView(generics.RetrieveAPIView):
    ''' Класс просмотра одного магазина '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityUpdateAPIView(generics.UpdateAPIView):
    ''' Класс обновления магазина '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityDestroyAPIView(generics.DestroyAPIView):
    ''' Класс удаления магазина '''
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]

class ProductViewSet(viewsets.ViewSet):
    '''вьюсет для продуктов'''
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsActiveUserPermissions]
