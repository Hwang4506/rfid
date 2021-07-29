from rest_framework import serializers
from .models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction, \
    Material_Warehouse_out, Production_Line_out, Finished_Product_Warehouse_out

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material_Warehouse
        fields = ['id', 'Receiving_Date_mw', 'RFID_Number_mw', 'Quantity_mw', 'Location_mw1']

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production_Line
        fields = ['id', 'Inline_Date', 'RFID_Number_pl', 'Quantity_pl', 'Location_pl1']

class FinishedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finished_Product_Warehouse
        fields = ['id', 'Receiving_Date_fw', 'RFID_Number_fw', 'Quantity_fw', 'Location_fw1']

class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'Work_Date', 'RFID_Number_dr', 'Gate_ID',
                  'Direction']

class MaterialoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material_Warehouse_out
        fields = ['id', 'Release_Date_mw', 'RFID_Number_mwout', 'Quantity_mwout', 'Location_mw']

class ProductionoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production_Line_out
        fields = ['id', 'Outline_Date', 'RFID_Number_plout', 'Quantity_plout', 'Location_pl']

class FinishedoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finished_Product_Warehouse_out
        fields = ['id', 'Release_Date_fw', 'RFID_Number_fwout', 'Quantity_fwout', 'Location_fw']