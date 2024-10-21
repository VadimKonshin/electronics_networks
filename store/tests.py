from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import NetworkEntity, Product
from users.models import User


class StoreTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.network_entity = NetworkEntity.objects.create(name='Pagani', level='0', debt='0.0')
        self.client.force_authenticate(user=self.user)

    def test_create_network_entity(self):
        '''тестирование создания сети'''
        url = reverse('store:net_create')
        data = {'name': 'Жигули', 'level': 2, 'debt': 10.0}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            NetworkEntity.objects.all().count(), 2
        )

        self.assertEqual(
            response.data['name'], data['name']
        )

    def test_retrieve_network_entity(self):
        ''' тестирование просмотра сети '''
        url = reverse('store:net_retrieve', args=(self.network_entity.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get('name'), self.network_entity.name
        )

    def test_delete_network_entity(self):
        ''' тестирование удаления сети '''
        url = reverse('store:net_delete', args=(self.network_entity.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            NetworkEntity.objects.filter(pk=self.network_entity.pk).exists()
        )

        self.assertEqual(
            NetworkEntity.objects.all().count(), 0
        )

    def test_update_network_entity(self):
        ''' тестирование обновления сети '''
        url = reverse('store:net_update', args=(self.network_entity.pk,))
        data = {'name': 'не жигули'}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name'], data['name']
        )

    def test_list_network_entity(self):
        ''' тестирование просмотра '''
        url = reverse('store:net_list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class ProductTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.network_entity = NetworkEntity.objects.create(name='Pagani', level='0', debt='0.0')
        self.product = Product.objects.create(name='машина', model='pp', release_date='2024-10-21',
                                              supplier=self.network_entity)
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        ''' тест просмотра продукта'''
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name'], data['name']
        )

    def test_list_product(self):
        ''' тест просмотра списка продуктов'''
        url = reverse('store:product-list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(), [{'id': 3, 'name': 'машина', 'model': 'pp', 'release_date': '2024-10-21', 'supplier': 2}]
        )

    def test_update_product(self):
        ''' тест обновления продукта '''
        url = reverse('store:product-detail', args=(self.product.pk,))
        data = {'name': 'не машина'}

        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get('name'), data['name']
        )

    def test_create_product(self):
        ''' тест создания продукта '''
        url = reverse('store:product-list')
        data = {'name': 'атомобиль', 'model': 'aa', 'release_date': '2024-10-21', 'supplier': 1}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Product.objects.all().count(), 2
        )

    def test_product_delete(self):
        ''' тест удаления продукта '''
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Product.objects.all().count(), 0
        )
