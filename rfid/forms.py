from django import forms
from rfid.models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production_Line
        fields = ['Inline_Date', 'RFID_Number_pl', 'Workline',
                  'Work_Details', 'Outline_Date']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material_Warehouse
        fields = ['Receiving_Date_mw', 'RFID_Number_mw', 'Product_ID',
                  'Quantity_mw', 'Location_mw', 'Release_Date_mw']

class FinishedForm(forms.ModelForm):
    class Meta:
        model = Finished_Product_Warehouse
        fields = ['Receiving_Date_fw', 'RFID_Number_fw', 'Quantity_fw',
                  'Location_fw', 'Release_Date_fw']

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['Work_Date', 'RFID_Number_dr', 'Gate_ID',
                  'Direction']