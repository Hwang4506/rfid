from django.contrib import admin

from .models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction


admin.site.register(Material_Warehouse)
admin.site.register(Production_Line)
admin.site.register(Finished_Product_Warehouse)
admin.site.register(Direction)