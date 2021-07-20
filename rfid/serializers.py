from rest_framework import serializers
from .models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material_Warehouse
        fields = ['id', 'Receiving_Date_mw', 'RFID_Number_mw', 'Product_ID',
                  'Quantity_mw', 'Location_mw', 'Release_Date_mw']

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production_Line
        fields = ['id', 'Inline_Date', 'RFID_Number_pl', 'Workline',
                  'Work_Details', 'Outline_Date']

class FinishedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finished_Product_Warehouse
        fields = ['id', 'Receiving_Date_fw', 'RFID_Number_fw', 'Quantity_fw',
                  'Location_fw', 'Release_Date_fw']

class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'Work_Date', 'RFID_Number_dr', 'Gate_ID',
                  'Direction']