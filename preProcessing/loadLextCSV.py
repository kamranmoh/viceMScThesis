""""
Function loads the measurement from the Olympus Lext in the .csv format and prepares it for further processing.

Usage: 
Input: filename = 
Output: 
        
Created by: Vice Rončević (s190075), 07.03.2021
"""

import pandas as pd
import numpy as np
import open3d as o3d

rawData = pd.read_csv("OpticalBench_beamSplitter.csv", header = None)
rawData = np.array(rawData)


# Issue: number of entries in the .csv file is not divideable by 3

#dataXYZ = np.zeros([(int((rawData.shape[1]-1) / 3)), 3])

#dataXYZ[:, 0] = rawData[0, ::3]

#pcd = o3d.geometry.PointCloud()
#pcd.points = o3d.utility.Vector3dVector(Data1)
#print(np.asarray(pcd.points))
#o3d.visualization.draw_geometries([pcd])