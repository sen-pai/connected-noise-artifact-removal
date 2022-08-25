import open3d as o3d 
import numpy as np


mesh = o3d.io.read_triangle_mesh("sample_stl/rahul_maxillary.stl")
mesh.compute_vertex_normals()


# o3d.visualization.draw_geometries([mesh])


pcd = o3d.geometry.PointCloud(mesh.vertices)
# # fit to unit cube
# pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
#           center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0.3, 0.9, size=(np.asarray(mesh.vertices).shape[0], 3)))
# o3d.visualization.draw_geometries([pcd])

print('voxelization')
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                            voxel_size=2)
o3d.visualization.draw_geometries([voxel_grid])