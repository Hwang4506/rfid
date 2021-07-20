# Generated by Django 3.1.3 on 2021-07-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finished_Product_Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiving_Date_fw', models.DateTimeField()),
                ('RFID_Number_fw', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity_fw', models.CharField(blank=True, max_length=50, null=True)),
                ('Location_fw', models.CharField(blank=True, max_length=50, null=True)),
                ('Release_Date_fw', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Material_Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiving_Date_mw', models.DateTimeField()),
                ('RFID_Number_mw', models.CharField(blank=True, max_length=50, null=True)),
                ('Product_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity_mw', models.CharField(blank=True, max_length=50, null=True)),
                ('Location_mw', models.CharField(blank=True, max_length=50, null=True)),
                ('Release_Date_mw', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Production_Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inline_Date', models.DateTimeField()),
                ('RFID_Number_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('Workline', models.CharField(blank=True, max_length=50, null=True)),
                ('Work_Details', models.CharField(blank=True, max_length=50, null=True)),
                ('Outline_Date', models.DateTimeField()),
            ],
        ),
    ]
