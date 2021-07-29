from django.contrib import admin

from .models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction, \
    Material_Warehouse_out, Production_Line_out, Finished_Product_Warehouse_out


admin.site.register(Material_Warehouse)
admin.site.register(Production_Line)
admin.site.register(Finished_Product_Warehouse)
admin.site.register(Direction)
admin.site.register(Material_Warehouse_out)
admin.site.register(Production_Line_out)
admin.site.register(Finished_Product_Warehouse_out)

