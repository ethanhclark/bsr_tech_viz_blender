import bpy
import csv
import os
import math
import datetime

def import_rotation_data(filepath):
    """Imports Z-axis rotation animation data from a CSV file and applies it to the corresponding objects."""
    if not os.path.exists(filepath):
        print("File not found: ", filepath)
        return
    
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        # Map object names to objects in the scene
        obj_map = {obj.name: obj for obj in bpy.data.objects}
        
        # Iterate through frames and apply animation data
        for row in reader:
            frame = int(row[0])
            
            for obj_name, z_rotation in zip(header[1:], row[1:]):
                if obj_name in obj_map:
                    obj = obj_map[obj_name]
                    obj.rotation_euler.z = math.radians(float(z_rotation))  # Convert degrees back to radians
                    obj.keyframe_insert(data_path="rotation_euler", index=2, frame=frame)
    
    print(f"Rotation data imported from {filepath}")
    
import_rotation_data("/Users/ethanclark/Desktop/BSI/bsr_tech_viz_blender/scripts/rotation-data-test.csv")
