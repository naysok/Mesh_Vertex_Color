import math
import time
import numpy as np


### Python3
### Using Numpy
from mesh_vertex_color import np_ray_triangle_intersection, util
rt = np_ray_triangle_intersection.RayTriangleIntersection()
ut = util.Util()


class MeshPointInsideOutside():


    """
    
    poly_mesh = 
    [
        [
            [v0.X, v0.Y, v0.Z],
            [v1.X, v1.Y, v1.Z], 
            [v2.X, v2.Y, v2.Z]
        ],        
        [
            [v0.X, v0.Y, v0.Z],
            [v1.X, v1.Y, v1.Z], 
            [v2.X, v2.Y, v2.Z]
        ],
        [
            [v0.X, v0.Y, v0.Z],
            [v1.X, v1.Y, v1.Z], 
            [v2.X, v2.Y, v2.Z]
        ],
    ]


    mesh = 
    [
        [v0.X, v0.Y, v0.Z],
        [v1.X, v1.Y, v1.Z], 
        [v2.X, v2.Y, v2.Z]
    ]
    
    """


    def poly_mesh_intersection(self, poly_mesh, point):
        
        ### Optimization with Numpy

        ### Transpose Matrix
        ### Nx3 >>> 3xN 
        poly_mesh_t = ut.transpose_matrix(poly_mesh)

        o = np.array([0, 0, 0]).reshape(1, 3)
        # o = o.reshape(1, 3)
        d = np.array(point).reshape(1, 3)
        # d = d.reshape(1, 3)
        v0 = np.array(poly_mesh_t[0])
        v1 = np.array(poly_mesh_t[1])
        v2 = np.array(poly_mesh_t[2])

        # print("o : {}".format(o))
        # print("o.shape : {}".format(o.shape))

        # print("d : {}".format(d))
        # print("d.shape : {}".format(d.shape))

        # print("v0 : {}".format(v0))
        # print("v0.shape : {}".format(v0.shape))

        ### Calc Intersection
        intersect_count = rt.calc_intersection(o, d, v0, v1, v2)
        
        return intersect_count


    def mesh_points_segmentation(self, poly_mesh, points):

        points_bool = []
        points_count = len(points)

        for i in range(points_count):

            tmp_pt = points[i]
            inout_count = self.poly_mesh_intersection(poly_mesh, tmp_pt)

            if inout_count%2 == 1:
                points_bool.append(True)
            else:
                points_bool.append(False)
        
        return points_bool