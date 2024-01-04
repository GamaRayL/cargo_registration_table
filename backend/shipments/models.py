from django.db import models

from constants import NULLABLE


class Shipment(models.Model):
    date = models.DateField(**NULLABLE, verbose_name='дата')
    time = models.TimeField(**NULLABLE, verbose_name='время')
    label = models.CharField(**NULLABLE, max_length=6, verbose_name='маркировка')
    document = models.TextField(**NULLABLE, verbose_name='документ поступления')
    vendor = models.CharField(**NULLABLE, max_length=100, verbose_name='поставщик')
    declared = models.IntegerField(**NULLABLE, verbose_name='заявлено')
    accepted = models.IntegerField(**NULLABLE, verbose_name='принято')
    counted = models.CharField(**NULLABLE, max_length=150, verbose_name='считал')
    driver = models.CharField(**NULLABLE, max_length=50, verbose_name='водитель')
