# Generated by Django 3.1.3 on 2021-07-27 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0002_material_warehouse_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production_Line_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Outline_Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('RFID_Number_plout', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity_plout', models.IntegerField(blank=True, default=0, null=True)),
                ('Location_pl', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='production_line',
            name='Outline_Date',
        ),
        migrations.RemoveField(
            model_name='production_line',
            name='Work_Details',
        ),
        migrations.RemoveField(
            model_name='production_line',
            name='Workline',
        ),
        migrations.AddField(
            model_name='production_line',
            name='Quantity_pl',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
