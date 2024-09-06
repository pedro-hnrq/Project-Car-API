from django.contrib import admin
from .models import Brand, Car


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand__name', 'color', 'factory_year', 'model_year', 'created_at',)
    search_fields = ('model',)
    list_filter = ('brand',)
