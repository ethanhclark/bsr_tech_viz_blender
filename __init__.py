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
import sys
import os

# Ensure Blender recognizes the add-on folder as a package
addon_name = os.path.basename(os.path.dirname(__file__))
if addon_name not in sys.modules:
    sys.path.append(os.path.dirname(__file__))

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

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        if not self.filepath.lower().endswith(".csv"):
            self.filepath += ".csv"
        
        print(f"Exporting to: {self.filepath}")  # Debugging output
        
        try:
            export_csv = importlib.import_module(__name__ + ".export_csv")
            export_csv.export_rotation_data(self.filepath)
            print("Export successful!")
        except Exception as e:
            print(f"Export failed: {e}")
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class CSV_OT_Import(bpy.types.Operator):
    bl_idname = "csv.import"
    bl_label = "Import CSV"
    bl_description = "Imports CSV data into Blender"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print(f"Importing from: {self.filepath}")  # Debugging output
        
        try:
            import_csv = importlib.import_module(__name__ + ".import_csv")
            import_csv.import_rotation_data(self.filepath)
            print("Import successful!")
        except Exception as e:
            print(f"Import failed: {e}")
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

classes = [CSV_PT_Panel, CSV_OT_Export, CSV_OT_Import]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
