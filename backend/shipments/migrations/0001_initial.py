# Generated by Django 5.0.1 on 2024-01-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='дата')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время')),
                ('label', models.CharField(blank=True, max_length=6, null=True, verbose_name='маркировка')),
                ('document', models.TextField(blank=True, null=True, verbose_name='документ поступления')),
                ('vendor', models.CharField(max_length=100, verbose_name='поставщик')),
                ('declared', models.IntegerField(max_length=5, verbose_name='заявлено')),
                ('accepted', models.IntegerField(max_length=5, verbose_name='принято')),
                ('counted', models.CharField(max_length=150, verbose_name='считал')),
                ('driver', models.CharField(max_length=50, verbose_name='водитель')),
            ],
        ),
    ]
