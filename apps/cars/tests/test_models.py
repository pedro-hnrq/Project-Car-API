from django.test import TestCase
from cars.models import Brand, Car
from django.contrib.auth import get_user_model

User = get_user_model()


class BrandModelTest(TestCase):

    def test_brand_creation(self):
        brand = Brand.objects.create(name='Test Brand', description='Test Description')
        self.assertEqual(brand.name, 'Test Brand')
        self.assertEqual(brand.description, 'Test Description')
        self.assertIsNotNone(brand.created_at)
        self.assertIsNotNone(brand.updated_at)

    def test_brand_str_representation(self):
        brand = Brand.objects.create(name='Test Brand')
        self.assertEqual(str(brand), 'Test Brand')


class CarModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')

    def test_car_creation(self):
        car = Car.objects.create(
            model='Test Model',
            brand=self.brand,
            factory_year=2020,
            model_year=2021,
            color='Red',
            owner=self.user,
            description='Test Car Description'
        )
        self.assertEqual(car.model, 'Test Model')
        self.assertEqual(car.brand, self.brand)
        self.assertEqual(car.factory_year, 2020)
        self.assertEqual(car.model_year, 2021)
        self.assertEqual(car.color, 'Red')
        self.assertEqual(car.owner, self.user)
        self.assertEqual(car.description, 'Test Car Description')
        self.assertIsNotNone(car.created_at)
        self.assertIsNotNone(car.updated_at)

    def test_car_str_representation(self):
        car = Car.objects.create(model='Test Model', brand=self.brand, owner=self.user)
        self.assertEqual(str(car), 'Test Model')
