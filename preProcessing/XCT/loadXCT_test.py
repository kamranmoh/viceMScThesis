""""
Script loads the point cloud in .pcd format and visualizes it.

Usage: 
Input: filename = 
Output: 
        
Created by: Vice Rončević (s190075), 13.03.2021
"""

import open3d as o3d

# Define custom visualization
def custom_draw_geometry(pcd):
    vis = o3d.visualization.Visualizer() # Initialize the main Visualizer class
    vis.create_window() 
    vis.add_geometry(pcd) # Add the geometry to the scene and create corresponding shaders
    vis.run()
    vis.destroy_window()

# Load the data
raw_pcd = o3d.io.read_point_cloud("RawRaw_stat_5.pcd", print_progress=True)

# Visualize the data
custom_draw_geometry(raw_pcd)

# TODO create json file with Render Options

#render_test = o3d.visualization.RenderOption()
#render_test
"""
o3d.visualization.draw_geometries([rawPCD],
                                  zoom=0.8,
                                  front=[0.4257, -0.2125, -0.8795], # Lookat vector of the camera
                                  lookat=[2.6172, 2.0475, 1.532],  # Front vector of the camera
                                  up=[-0.0694, -0.9768, 0.2024], # Up vector of the camera
                                  window_name="Testing",
                                  width=720,
                                  height=720                        
                                  )  
"""                            