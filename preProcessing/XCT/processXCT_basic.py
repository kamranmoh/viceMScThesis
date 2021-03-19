""""
Script loads the point cloud in .pcd format and performs basic processing on it.

Usage: 
Input: 
Output: 
        
Created by: Vice Rončević (s190075), 19.03.2021
"""

import open3d as o3d
import numpy as np

# Define custom general purpose visualizer as a data post processing utility
# At the moment it can deal with two objects
def customDrawGeometry(geom_obj_1, geom_obj_2):
    # Initialize the main Visualizer class
    vis = o3d.visualization.Visualizer() 
    vis.create_window(
        window_name = "Data post processing", 
        width = 720, 
        height = 720, 
        left = 25,
        top = 25 
        )

    # Add the geometry to the scene and create corresponding shaders
    vis.add_geometry(geom_obj_1)
    vis.add_geometry(geom_obj_2) 

    # Rendering options
    opt = vis.get_render_option()
    opt.show_coordinate_frame = True
    opt.point_size = 10
    opt.light_on = True

    # Change the view
    view = vis.get_view_control()
    view.rotate(250, 250)

    # Run the visualization
    vis.run()
    vis.destroy_window()

# Load the point cloud data
raw_pcd = o3d.io.read_point_cloud("RawRaw_stat_5.pcd", print_progress = True)

# Compute mean and covariance of the point clouds coordinates
mean_and_cov = raw_pcd.compute_mean_and_covariance()
print("Mean of point values per axis:", mean_and_cov[0])
print("Covariance matrix of the point cloud axes:\n", mean_and_cov[1])
print("\n")

# Get the aligned bounding box object of the point cloud and the points that define it
bounding_box = raw_pcd.get_oriented_bounding_box()

# Vertices 
box_points = bounding_box.get_box_points()
# Convert to numpy
box_points = np.asarray(box_points)

# Center point
center_point = bounding_box.get_center()
# Convert to Open3D format
center_point_pcd = o3d.geometry.PointCloud()
center_point = np.reshape(center_point, (1,3))
center_point_pcd.points = o3d.utility.Vector3dVector(center_point)

# Draw the resulting box using the LineSet from open3d.geometry
line_set = o3d.geometry.LineSet()
line_set = line_set.create_from_oriented_bounding_box(bounding_box)

# Visualize
customDrawGeometry(line_set, center_point_pcd)

