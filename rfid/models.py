from django.db import models
from django.utils import timezone

class Material_Warehouse(models.Model):
    Receiving_Date_mw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_mw = models.CharField(max_length=50, null=True, blank=True)
    Quantity_mw = models.IntegerField(default=0, null=True, blank=True)
    Location_mw1 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_mw

class Material_Warehouse_out(models.Model):
    Release_Date_mw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_mwout = models.CharField(max_length=50, null=True, blank=True)
    Quantity_mwout = models.IntegerField(default=0, null=True, blank=True)
    Location_mw = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_mwout

class Production_Line(models.Model):
    Inline_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_pl = models.CharField(max_length=50, null=True, blank=True)
    Quantity_pl = models.IntegerField(default=0, null=True, blank=True)
    Location_pl1 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_pl

class Production_Line_out(models.Model):
    Outline_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_plout = models.CharField(max_length=50, null=True, blank=True)
    Quantity_plout = models.IntegerField(default=0, null=True, blank=True)
    Location_pl = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_plout

class Finished_Product_Warehouse(models.Model):
    Receiving_Date_fw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_fw = models.CharField(max_length=50, null=True, blank=True)
    Quantity_fw = models.IntegerField(default=0, null=True, blank=True)
    Location_fw1 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_fw

class Finished_Product_Warehouse_out(models.Model):
    Release_Date_fw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_fwout = models.CharField(max_length=50, null=True, blank=True)
    Quantity_fwout = models.IntegerField(default=0, null=True, blank=True)
    Location_fw = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_fwout

class Direction(models.Model):
    Work_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_dr = models.CharField(max_length=50, null=True, blank=True)
    Gate_ID = models.CharField(max_length=50, null=True, blank=True)
    Direction = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_dr