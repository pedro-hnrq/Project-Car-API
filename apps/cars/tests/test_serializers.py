from django.test import TestCase
from rest_framework.exceptions import ValidationError
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

User = get_user_model()


class BrandSerializerTest(TestCase):

    def test_brand_serializer_valid(self):
        data = {'name': 'Test Brand', 'description': 'Test Description'}
        serializer = BrandModelSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_brand_serializer_duplicate_name(self):
        Brand.objects.create(name='Test Brand')
        data = {'name': 'Test Brand'}
        serializer = BrandModelSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)


class CarSerializerTest(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.factory = APIRequestFactory()

    def test_car_serializer_valid(self):
        data = {
            'model': 'Test Model',
            'brand': self.brand.id,
            'factory_year': 2020,
            'model_year': 2021,
            'color': 'Red',
            'description': 'Test Car Description'
        }
        request = self.factory.get('/')
        request.user = self.user
        serializer = CarModelSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid())

    def test_car_serializer_invalid_brand(self):
        data = {
            'model': 'Test Model',
            'brand': 9999,
            'factory_year': 2020,
            'model_year': 2021,
            'color': 'Red',
            'description': 'Test Car Description'
        }
        request = self.factory.get('/')
        request.user = self.user
        serializer = CarModelSerializer(data=data, context={'request': request})
        # O serializer passa na validação inicial; o erro só ocorre no save()
        self.assertTrue(serializer.is_valid(), msg="O serializer deve ser válido até chamar save()")
        with self.assertRaises(ValidationError) as context:
            serializer.save()
        self.assertIn("Marca não encontrada", str(context.exception))

    def test_car_serializer_create(self):
        data = {
            'model': 'Test Model',
            'brand': self.brand.id,
            'factory_year': 2020,
            'model_year': 2021,
            'color': 'Red',
            'description': 'Test Car Description'
        }
        request = self.factory.get('/')
        request.user = self.user
        serializer = CarModelSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        car = serializer.save()
        self.assertEqual(car.model, 'Test Model')
        self.assertEqual(car.brand, self.brand)
        self.assertEqual(car.owner, self.user)

    def test_car_serializer_update(self):
        car = Car.objects.create(model='Old Model', brand=self.brand, owner=self.user)
        new_brand = Brand.objects.create(name='New Brand')
        data = {
            'model': 'New Model',
            'brand': new_brand.id,
            'factory_year': 2022,
            'model_year': 2023,
            'color': 'Blue',
            'description': 'New Car Description'
        }
        request = self.factory.get('/')
        request.user = self.user
        serializer = CarModelSerializer(car, data=data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        updated_car = serializer.save()
        self.assertEqual(updated_car.model, 'New Model')
        self.assertEqual(updated_car.brand, new_brand)
        self.assertEqual(updated_car.color, 'Blue')
