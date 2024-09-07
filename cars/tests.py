from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cars.models import Brand, Car
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class JWTAuthMixin:
    def obtain_jwt_token(self):
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.username,
            'password': self.password
        }, format='json')
        return response.data['access']

    def setUp(self):
        # Criação do superusuário
        self.username = 'admin'
        self.password = 'adminpassword'
        self.user = User.objects.create_superuser(username=self.username, password=self.password)
        self.access_token = self.obtain_jwt_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

class BrandTests(JWTAuthMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.list_url = reverse('brand-list')
        self.detail_url = lambda pk: reverse('brand-detail', kwargs={'pk': pk})

    def test_create_brand(self):
        data = {'name': 'Toyota', 'description': 'Japanese car brand'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 1)
        self.assertEqual(Brand.objects.get().name, 'Toyota')

    def test_get_brands(self):
        Brand.objects.create(name='Toyota', description='Japanese car brand')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_brand(self):
        brand = Brand.objects.create(name='Toyota', description='Japanese car brand')
        response = self.client.patch(self.detail_url(brand.id), {'name': 'Honda'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.get().name, 'Honda')

    def test_delete_brand(self):
        brand = Brand.objects.create(name='Toyota', description='Japanese car brand')
        response = self.client.delete(self.detail_url(brand.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.count(), 0)

class CarTests(JWTAuthMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.brand = Brand.objects.create(name='Toyota')
        self.list_url = reverse('car-list')
        self.detail_url = lambda pk: reverse('car-detail', kwargs={'pk': pk})

    def test_create_car(self):
        data = {
            'model': 'Corolla',
            'brand': self.brand.id,
            'factory_year': 2020,
            'model_year': 2021,
            'color': 'Red',
            'owner': self.user.id,
            'description': 'Compact car'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(Car.objects.get().model, 'Corolla')

    def test_get_cars(self):
        Car.objects.create(
            model='Corolla', brand=self.brand, factory_year=2020,
            model_year=2021, color='Red', owner=self.user, description='Compact car'
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_car(self):
        car = Car.objects.create(
            model='Corolla', brand=self.brand, factory_year=2020,
            model_year=2021, color='Red', owner=self.user, description='Compact car'
        )
        response = self.client.patch(self.detail_url(car.id), {'color': 'Blue'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Car.objects.get().color, 'Blue')

    def test_delete_car(self):
        car = Car.objects.create(
            model='Corolla', brand=self.brand, factory_year=2020,
            model_year=2021, color='Red', owner=self.user, description='Compact car'
        )
        response = self.client.delete(self.detail_url(car.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)
