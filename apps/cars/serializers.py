from rest_framework import serializers
from cars.models import Brand, Car
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    def validate_name(self, value):
        if self.instance is None and Brand.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Já existe uma marca com este nome.")
        return value


class CarModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)     
    brand = serializers.CharField() 
    class Meta:
        model = Car
        fields = [
            'id', 
            'model',
            'brand',             
            'color',
            'factory_year',
            'model_year',  
            'description',            
            'owner',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        # Recupera o usuário autenticado a partir do contexto
        request = self.context.get("request")
        if not request or request.user.is_anonymous:
            raise serializers.ValidationError("Usuário autenticado é obrigatório.")

        owner = request.user

        # Processa o campo 'brand'
        brand_data = validated_data.pop('brand')
        try:
            # Tenta interpretar como ID
            brand_id = int(brand_data)
            brand = Brand.objects.get(id=brand_id)
        except (ValueError, Brand.DoesNotExist):
            # Se não for um número ou não existir, tenta buscar pelo nome
            try:
                brand = Brand.objects.get(name=brand_data)
            except Brand.DoesNotExist:
                raise serializers.ValidationError("Marca não encontrada com o ID ou nome fornecido.")
        
        car = Car.objects.create(brand=brand, owner=owner, **validated_data)
        return car

    def update(self, instance, validated_data):
        # Se o campo 'brand' for enviado, processa-o
        brand_data = validated_data.pop('brand', None)
        if brand_data is not None:
            try:
                # Tenta interpretar como ID
                brand_id = int(brand_data)
                brand = Brand.objects.get(id=brand_id)
            except (ValueError, Brand.DoesNotExist):
                # Se não for número ou não existir, tenta buscar pelo nome
                try:
                    brand = Brand.objects.get(name=brand_data)
                except Brand.DoesNotExist:
                    raise serializers.ValidationError("Marca não encontrada com o ID ou nome fornecido.")
            instance.brand = brand

        # Atualiza os demais campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

        