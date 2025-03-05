import bpy
import csv
import os
import math
import datetime

def normalize_angle(degrees):
    """Convert angles to the -180 to 180 range."""
    degrees = degrees % 360  # Ensure within 0-360
    if degrees > 180:
        degrees -= 360  # Shift to -180 to 180 range
    return degrees

def export_rotation_data(filepath):
    """Exports the Z-axis rotation animation data of selected objects to a CSV file in degrees."""
    scene = bpy.context.scene
    selected_objects = [obj for obj in bpy.context.selected_objects if obj.animation_data]
    
    if not selected_objects:
        print("No animated objects selected.")
        return
    
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        header = ["Frame"] + [obj.name for obj in selected_objects]
        writer.writerow(header)
        
        # Get frame range
        start_frame = scene.frame_start
        end_frame = scene.frame_end
        
        # Iterate through frames
        for frame in range(start_frame, end_frame + 1):
            scene.frame_set(frame)
            row = [frame]
            
            for obj in selected_objects:
                z_rotation = math.degrees(obj.rotation_euler.z)  # Convert local rotation to degrees
                z_rotation = normalize_angle(z_rotation)  # Normalize to -180 to 180 range
                row.append(z_rotation)
            
            writer.writerow(row)
    
    print(f"Rotation data exported to {filepath}")
