import math
import time


### IronPython 2
from mesh_vertex_color import irp_ray_triangle_intersection
reload(irp_ray_triangle_intersection)
rt = irp_ray_triangle_intersection.RayTriangleIntersection()


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

        ### Poly-Mesh >>> Mesh
        for i in range(mesh_count):
            
            tmp_mesh = poly_mesh[i]
            in_out_bool = self.mesh_intersect(tmp_mesh, point)

            if in_out_bool != None:
                in_out_count += 1
            
        return in_out_count
