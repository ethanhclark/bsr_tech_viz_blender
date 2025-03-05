bl_info = {
    "name": "CSV Import/Export Add-on",
    "blender": (3, 0, 0),
    "category": "Import-Export",
    "author": "Your Name",
    "version": (1, 0, 0),
    "description": "Adds CSV import/export functionality to Blender",
    "location": "View3D > Sidebar > CSV Tools",
    "warning": "",
    "support": "COMMUNITY"
}

import bpy
import importlib
import os

# Import custom scripts
from . import export_csv, import_csv
importlib.reload(export_csv)
importlib.reload(import_csv)

class CSV_PT_Panel(bpy.types.Panel):
    bl_label = "CSV Tools"
    bl_idname = "CSV_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CSV Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator("csv.export", text="Export CSV")
        layout.operator("csv.import", text="Import CSV")

class CSV_OT_Export(bpy.types.Operator):
    bl_idname = "csv.export"
    bl_label = "Export CSV"
    bl_description = "Exports CSV data from Blender"

    def execute(self, context):
        export_csv.export_csv()
        return {'FINISHED'}

class CSV_OT_Import(bpy.types.Operator):
    bl_idname = "csv.import"
    bl_label = "Import CSV"
    bl_description = "Imports CSV data into Blender"

    def execute(self, context):
        import_csv.import_csv()
        return {'FINISHED'}

classes = [CSV_PT_Panel, CSV_OT_Export, CSV_OT_Import]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
