from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(_('Nome'), max_length=100, db_index=True)
    description = models.TextField(_('Descrição'), null=True, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        db_table = "brands"
        ordering = ['name']
        verbose_name = _('Marca')
        verbose_name_plural = _('Marcas')

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(_('Modelo'), max_length=100, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    factory_year = models.IntegerField(_('Ano de fabricação'), null=True)
    model_year = models.IntegerField(_('Ano do modelo'), null=True)
    color = models.CharField(_('Cor'), max_length=50, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                              verbose_name='Proprietário')
    description = models.TextField(_('Descrição'), null=True, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        db_table = "cars"
        ordering = ['model']
        verbose_name = _('Carro')
        verbose_name_plural = _('Carros')

    def __str__(self):
        return self.model
