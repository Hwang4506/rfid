# Generated by Django 3.1.3 on 2021-07-06 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0006_auto_20210705_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished_product_warehouse',
            name='Receiving_Date_fw',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='finished_product_warehouse',
            name='Release_Date_fw',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='production_line',
            name='Inline_Date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='production_line',
            name='Outline_Date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]