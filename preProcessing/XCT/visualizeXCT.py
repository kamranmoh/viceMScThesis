""""
Script loads the point cloud in .pcd format and visualizes it
using custom rendering and viewing options. 
Furthemore, it extrapolates and visualized the depth image from the 
point cloud, captured in the the initial frame that has been visualized.

Usage: load the point cloud data using the open3d.io.read_point_cloud function, observe the output (TO BE IMPROVED)
Input: 
Output: 
        
Created by: Vice Rončević (s190075), 13.03.2021
"""

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# Define custom point cloud visualization and extrapolation of extra data
def customDrawPCD(pcd):
    # Initialize the main Visualizer class
    vis = o3d.visualization.Visualizer() 
    vis.create_window(
        window_name = "Point Cloud", 
        width = 720, 
        height = 720, 
        left = 25,
        top = 25 
        )

    # Add the geometry to the scene and create corresponding shaders
    vis.add_geometry(pcd) 

    # Rendering options
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0]) # RGB
    opt.point_size = 0.2
    opt.show_coordinate_frame = True
    opt.light_on = True

    # Change the view
    view = vis.get_view_control()
    view.rotate(250, 250)

    # Extrapolate depth in a float buffer, returns Image geometry type
    depthImage = vis.capture_depth_float_buffer(do_render = True)

    # Run the visualization
    vis.run()
    vis.destroy_window()

    return depthImage


# Load the point cloud data
raw_pcd = o3d.io.read_point_cloud("RawRaw_stat_5.pcd", print_progress = True)

# Paint the point cloud data uniformly
#raw_pcd = raw_pcd.paint_uniform_color(np.asarray([1, 0, 0]))

# Visualize the point cloud and get the depth image
depthImage = customDrawPCD(raw_pcd)

# Visualize the depth image
plt.imshow(np.asarray(depthImage))
plt.show()

    