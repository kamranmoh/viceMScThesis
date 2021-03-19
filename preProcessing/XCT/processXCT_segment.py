""""
Script loads 2 cropped point clouds. Then it computes the distance between them,
and segments a RANSAC plane in one of them and subsequently visualizes the cloud
with the planes.

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
    opt.point_size = 1
    opt.light_on = True

    # Change the view
    view = vis.get_view_control()
    view.rotate(250, 250)

    # Run the visualization
    vis.run()
    vis.destroy_window()

# Load the point cloud data
pcd1 = o3d.io.read_point_cloud("groove5_selection_left.ply", print_progress = True)
pcd2 = o3d.io.read_point_cloud("groove5_selection_right.ply", print_progress = True)

# Compute the distance between each point in the the two clouds
distance = pcd1.compute_point_cloud_distance(pcd2)
distance = np.asarray(distance)

# Segment a plane in one point cloud
plane_model, inliers = pcd1.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)

inlier_cloud = pcd1.select_by_index(inliers)
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd1.select_by_index(inliers, invert=True)
outlier_cloud.paint_uniform_color([0, 0, 1.0])

# Visualize two clouds
customDrawGeometry(pcd1, pcd2)

# Visualize the first cloud with the segmented plane
customDrawGeometry(inlier_cloud, outlier_cloud)