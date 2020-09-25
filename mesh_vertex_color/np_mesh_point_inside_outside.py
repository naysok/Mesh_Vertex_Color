import math
import time
import numpy as np


### Python3
### Using Numpy
from mesh_vertex_color import np_ray_triangle_intersection
rt = np_ray_triangle_intersection.RayTriangleIntersection()


class MeshPointInsideOutside():


    """
    
    mesh = [[v0.X, v0.Y, v0.Z], [v1.X, v1.Y, v1.Z], [v2.X, v2.Y, v2.Z]]
    
    """


    def mesh_intersect(self, mesh, point):
        
        ### Optimization with Numpy

        ### ray_triangle_intersection
        ### rt.calc_intersection(o, d, v0, v1, v2)
        
        o = [0, 0, 0]
        d = point
        v0 = mesh[0]
        v1 = mesh[1]
        v2 = mesh[2]

        # bool_intersect = rt.calc_intersection(o, d, v0, v1, v2)
        
        return bool_intersect


    def poly_mesh_intersection(self, poly_mesh, points):
        
        ### Optimization with Numpy
        
        # if intersect_count%2 == 1:
        #     new_list.append(white)
        # else:
        #     new_list.append(blank)
        pass


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
