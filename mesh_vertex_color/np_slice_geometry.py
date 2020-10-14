import math
import time


### Python3

from . import np_mesh_point_inside_outside
mio = np_mesh_point_inside_outside.MeshPointInsideOutside()

from . import image_processing, stl_parser
imp = image_processing.ImageProcessing()
stp = stl_parser.StlParser()


class SliceGeometry():


    def intersection_test(self, stl_path, point):

        ### Performance Test

        time_0 = time.time()

        ### STL >> [v0, v1, v2]
        meshes = stp.stl2meshes(stl_path)
        # print(len(meshes))

        time_1 = time.time()

        intersect_count = mio.poly_mesh_intersection(meshes, point)
        print("[Test] Intersect Count : {}".format(intersect_count))

        if intersect_count%2 == 0:
            print("[Test] Outside!!")
        else:
            print("[Test] Inside!!")
        
        time_2 = time.time()

        print("Open and Load STL : {} Sec".format(time_1 - time_0))
        print("Calc Point Inside/OutSide : {} Sec".format(time_2 - time_1))
        
        ### Core i5 (MacBook Pro 2014)
        ### Open and Load STL : 0.05614614486694336 Sec
        ### Calc Point Inside/OutSide : 0.019470930099487305 Sec


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

        ### Poly-Mesh Point Segment
        intersect_count = mio.poly_mesh_intersection(mesh, pts)
        # # print(intersect_count)
        
        # new_tuple = tuple(new_list)

        return pts


    def define_mask(self, stl_path, img_path, volume_size, layer_height, down_sampling_xy):

        ### STL >> [v0, v1, v2]
        meshes = stp.stl2meshes(stl_path)
        print("Mesh Count : {}".format(len(meshes)))

        layer_count = int(volume_size / layer_height)
        print("Layer Count : {}".format(layer_count))

        canvas_size = int(volume_size / down_sampling_xy)
        canvas = imp.create_canvas(canvas_size)
        data_im = canvas.getdata()


        # for i in range(layer_count):
        for i in range(14815, 14816):

            h_slicing = float(i * layer_height)
            h_slicing = 400.0

            print("Processing - Layer : {}".format(i))
            print("Processing - Height : {}".format(h_slicing))

            mask = self.slice_mesh(meshes, volume_size, h_slicing, down_sampling)
            # print(mask)

            # canvas.putdata(mask)
            # imp.export_image(canvas, img_path)

        return 


    def render():
        pass


