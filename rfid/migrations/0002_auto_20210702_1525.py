# Generated by Django 3.1.3 on 2021-07-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material_warehouse',
            name='Quantity_mw',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
