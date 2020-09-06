import math

from . import ray_triangle_intersection
rt = ray_triangle_intersection.RayTriangleIntersection()


### Build Module via Cython
# from . import cy_ray_triangle_intersection
# rt = cy_ray_triangle_intersection.RayTriangleIntersection()


class MeshPointInsideOutside():


    """
    
    mesh = [[v0.X, v0.Y, v0.Z], [v1.X, v1.Y, v1.Z], [v2.X, v2.Y, v2.Z]]
    
    """


    def mesh_intersect(self, mesh, point):
        
        ### ray_triangle_intersection
        ### rt.calc_intersection(o, d, v0, v1, v2)
        
        o = [0, 0, 0]
        d = point
        v0 = mesh[0]
        v1 = mesh[1]
        v2 = mesh[2]

        bool_intersect = rt.calc_intersection(o, d, v0, v1, v2)
        
        return bool_intersect


    def poly_mesh_intersection(self, poly_mesh, point):
        
        in_out_count = 0
        mesh_count = len(poly_mesh)

        for i in range(mesh_count):
            
            tmp_mesh = poly_mesh[i]
            in_out_bool = self.mesh_intersect(tmp_mesh, point)

            if in_out_bool != None:
                in_out_count += 1
            
        # print(in_out_count)
        return in_out_count


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

