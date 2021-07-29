# Generated by Django 3.1.3 on 2021-07-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0004_auto_20210728_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='finished_product_warehouse',
            name='Location_fw1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='material_warehouse',
            name='Location_mw1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='production_line',
            name='Location_pl1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]