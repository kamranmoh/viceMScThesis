""""
Script loads the STEP GAUGE point cloud in .pcd format 
and allows the user to either perform manual cropping of
the geometry or to pick some points from it.

Usage: 
Input: 
Output: 
        
Created by: Vice Rončević (s190075), 19.03.2021
"""

import open3d as o3d
import numpy as np

# TODO Standardize https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it

def demoCropGeometry(pcd):
    print("Manual cropping visualizer & export")
    print(
        "1) Press 'Y' twice to align geometry with negative direction of y-axis"
    )
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Drag for rectangle selection,")
    print("   or use ctrl + left click for polygon selection")
    print("4) Press 'C' to get a selected geometry and to save it")
    print("5) Press 'F' to switch to freeview mode")
    o3d.visualization.draw_geometries_with_editing([pcd],
    window_name = "Point Cloud", 
        width = 720, 
        height = 720, 
        left = 25,
        top = 25  
        )

def pick_points(pcd):
    print("Point picking visualizer")
    print(
        "1) Please pick at least three correspondences using [shift + left click]"
    )
    print("   Press [shift + right click] to undo point picking")
    print("2) After picking points, press 'Q' to close the window")
    vis = o3d.visualization.VisualizerWithEditing()
    vis.create_window(
        window_name = "Point Picking", 
        width = 720, 
        height = 720, 
        left = 25,
        top = 25 
        )
    vis.add_geometry(pcd)
    vis.run() 
    vis.destroy_window()
    print("")
    return vis.get_picked_points()

# Load the point cloud data
raw_pcd = o3d.io.read_point_cloud("RawRaw_stat_5.pcd", print_progress = True)

demoCropGeometry(raw_pcd)
#pick_points(raw_pcd)

