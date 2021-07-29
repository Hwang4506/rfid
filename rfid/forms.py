from django import forms
from rfid.models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, \
    Direction, Material_Warehouse_out, Production_Line_out, Finished_Product_Warehouse_out


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production_Line
        fields = ['Inline_Date', 'RFID_Number_pl', 'Quantity_pl', "Location_pl1"]

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material_Warehouse
        fields = ['Receiving_Date_mw', 'RFID_Number_mw', 'Quantity_mw', "Location_mw1"]

class FinishedForm(forms.ModelForm):
    class Meta:
        model = Finished_Product_Warehouse
        fields = ['Receiving_Date_fw', 'RFID_Number_fw', 'Quantity_fw', "Location_fw1"]

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['Work_Date', 'RFID_Number_dr', 'Gate_ID',
                  'Direction']

class MaterialoutForm(forms.ModelForm):
    class Meta:
        model = Material_Warehouse_out
        fields = ['Release_Date_mw', 'RFID_Number_mwout', 'Quantity_mwout', 'Location_mw']

class ProductionoutForm(forms.ModelForm):
    class Meta:
        model = Production_Line_out
        fields = ['Outline_Date', 'RFID_Number_plout', 'Quantity_plout', 'Location_pl']

class FinishedoutoutForm(forms.ModelForm):
    class Meta:
        model = Finished_Product_Warehouse_out
        fields = ['Release_Date_fw', 'RFID_Number_fwout', 'Quantity_fwout', 'Location_fw']