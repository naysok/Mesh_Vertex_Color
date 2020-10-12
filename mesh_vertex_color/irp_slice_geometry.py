import math
import time

### IronPython 2
from . import irp_mesh_point_inside_outside
mio = irp_mesh_point_inside_outside.MeshPointInsideOutside()

from . import stl_parser
stp = stl_parser.StlParser()


class SliceGeometry():


    def intersection_test(self, stl_path, point):

        ### Performance Test

        # time_0 = time.time()

        ### STL >> [v0, v1, v2]
        meshes = stp.stl2meshes(stl_path)
        # print(len(meshes))

        # time_1 = time.time()

        intersect_count = mio.poly_mesh_intersection(meshes, point)
        print("Intersect Count : {}".format(intersect_count))


        if intersect_count%2 == 0:
            print("Outside!!")
        else:
            print("Inside!!")

        ### Time_12 : 0.02240610122680664Sec

        # time_2 = time.time()

        # time_01 = time1 - time0
        # time_12 = time2 - time1

        # print("Time_01 : {}Sec".format(time_01))
        # print("Time_12 : {}Sec".format(time_12))


    def slice_mesh(self, mesh, volume_size, slice_height, down_sampling):
        
        grid_size_ds = int(volume_size / down_sampling)
        
        new_list = []
        in_out_bool = []

        white = tuple([255, 255, 255, 255])
        blank = tuple([0, 0, 0, 255])

        pts = []
        for i in range(grid_size_ds):

            # print(i)

            for j in range(grid_size_ds):
                    
                ### Point
                pt = [
                    float(i * down_sampling),
                    float(j * down_sampling),
                    float(slice_height)]
                
                # pts.append(pt)
                intersect_count = mio.poly_mesh_intersection(mesh, pt)
                # print(intersect_count)
        
        # new_tuple = tuple(new_list)

        return pts


    def define_mask(self, stl_path, img_path, volume_size, layer_height, down_sampling_xy):
        pass


    def render():
        pass