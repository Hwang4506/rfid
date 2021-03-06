# Generated by Django 3.1.3 on 2021-07-28 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0003_auto_20210727_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finished_Product_Warehouse_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Release_Date_fw', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('RFID_Number_fwout', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity_fwout', models.IntegerField(blank=True, default=0, null=True)),
                ('Location_fw', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='finished_product_warehouse',
            name='Location_fw',
        ),
        migrations.RemoveField(
            model_name='finished_product_warehouse',
            name='Release_Date_fw',
        ),
    ]
