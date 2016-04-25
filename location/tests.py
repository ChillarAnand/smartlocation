from rest_framework.test import APITestCase

from django.core.urlresolvers import reverse
from rest_framework import status

from .models import Provider, ServiceArea


class ProviderTestCase(APITestCase):
    def test_create_provider(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('provider-list')
        data = {'name': 'foo'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)

    def test_list_provider(self):
        url = reverse('provider-list')
        data = {'name': 'foo'}
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'foo')

    def test_update_provider_name(self):
        url = reverse('provider-list')
        data = {'name': 'foo'}
        response = self.client.post(url, format='json', data=data)
        assert response.status_code == status.HTTP_201_CREATED
        url = reverse('provider-detail', args=[response.data['pk']])
        data['name'] = 'Foo'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        assert resp.data['name'] == data['name']

    def test_delete_provider(self):
        url = reverse('provider-list')
        data = {'name': 'foo'}
        response = self.client.post(url, format='json', data=data)
        assert response.status_code == status.HTTP_201_CREATED
        url = reverse('provider-detail', args=[response.data['pk']])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.delete(url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)


class ServiceAreaTestCase(APITestCase):

    def setUp(self):
        response = self.client.post(reverse('provider-list'), format='json', data={'name': 'foo'})
        provider_url = reverse('provider-detail', args=[response.data['pk']])
        self.data = {
            'name': 'foo',
            'provider': provider_url,
            'price': 200.01,
            'polygon':  [
                [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]
            ],
        }

    def test_create_service_area(self):
        url = reverse('servicearea-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)

    def test_list_service_areas(self):
        url = reverse('servicearea-list')
        self.client.post(url, self.data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'foo')

    def test_update_servicearea_name(self):
        url = reverse('servicearea-list')
        response = self.client.post(url, format='json', data=self.data)
        assert response.status_code == status.HTTP_201_CREATED
        url = reverse('servicearea-detail', args=[response.data['pk']])
        self.data['name'] = 'Foo'
        resp = self.client.patch(url, data=self.data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        assert resp.data['name'] == self.data['name']

    def test_delete_servicearea(self):
        url = reverse('servicearea-list')
        response = self.client.post(url, format='json', data=self.data)
        assert response.status_code == status.HTTP_201_CREATED
        url = reverse('servicearea-detail', args=[response.data['pk']])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.delete(url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_find_service_areas(self):
        url = reverse('servicearea-list')
        response = self.client.post(url, format='json', data=self.data)
        url = "{}?latitude={}&longitude={}".format(reverse('find_service_areas'), 0.6, 100.5)
        response = self.client.get(url, format='json')
        self.assertEqual(response.data[0][0], 'foo')
