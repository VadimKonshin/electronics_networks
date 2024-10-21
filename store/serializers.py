from rest_framework import serializers

from store.models import NetworkEntity, Product


class NetworkEntitySerializers(serializers.ModelSerializer):
    ''' Сериалайзер сети '''
    class Meta:
        model = NetworkEntity
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    ''' Сериалайзер продукта '''
    class Meta:
        model = Product
        fields = '__all__'
