from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from cars.models import Brand, Car
from django.contrib.auth import get_user_model

User = get_user_model()


class CarViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.brand = Brand.objects.create(name='Test Brand')
        self.car = Car.objects.create(model='Test Model', brand=self.brand, owner=self.user)
        self.client.force_authenticate(user=self.user)
        Car.objects.create(model='Test Model2', brand=self.brand, owner=self.user)
        Car.objects.create(model='Test Model3', brand=self.brand, owner=self.user)
        Car.objects.create(model='Test Model4', brand=self.brand, owner=self.user)

    def test_car_list(self):
        response = self.client.get(reverse('car-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_car_create(self):
        data = {
            'model': 'New Model',
            'brand': self.brand.id,
            'factory_year': 2022,
            'model_year': 2023,
            'color': 'Blue',
            'description': 'New Car Description'
        }
        response = self.client.post(reverse('car-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 5)
