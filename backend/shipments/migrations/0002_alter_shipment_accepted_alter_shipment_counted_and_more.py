# Generated by Django 5.0.1 on 2024-01-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='accepted',
            field=models.IntegerField(blank=True, null=True, verbose_name='принято'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='counted',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='считал'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='declared',
            field=models.IntegerField(blank=True, null=True, verbose_name='заявлено'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='driver',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='водитель'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='vendor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='поставщик'),
        ),
    ]