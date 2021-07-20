from django.db import models
from django.utils import timezone

class Material_Warehouse(models.Model):
    Receiving_Date_mw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_mw = models.CharField(max_length=50, null=True, blank=True)
    Product_ID = models.CharField(max_length=50, null=True, blank=True)
    Quantity_mw = models.IntegerField(default=0, null=True, blank=True)
    Location_mw = models.CharField(max_length=50, null=True, blank=True)
    Release_Date_mw = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_mw

class Production_Line(models.Model):
    Inline_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_pl = models.CharField(max_length=50, null=True, blank=True)
    Workline = models.CharField(max_length=50, null=True, blank=True)
    Work_Details = models.CharField(max_length=50, null=True, blank=True)
    Outline_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_pl

class Finished_Product_Warehouse(models.Model):
    Receiving_Date_fw = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_fw = models.CharField(max_length=50, null=True, blank=True)
    Quantity_fw = models.IntegerField(default=0, null=True, blank=True)
    Location_fw = models.CharField(max_length=50, null=True, blank=True)
    Release_Date_fw = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_fw

class Direction(models.Model):
    Work_Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RFID_Number_dr = models.CharField(max_length=50, null=True, blank=True)
    Gate_ID = models.CharField(max_length=50, null=True, blank=True)
    Direction = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RFID_Number_dr