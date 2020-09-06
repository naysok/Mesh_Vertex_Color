import math

from . import mesh_point_inside_outside
from . import image_processing
from . import stl_parser

mio = mesh_point_inside_outside.MeshPointInsideOutside()
imp = image_processing.ImageProcessing()
stp = stl_parser.StlParser()


### Build Module via Cython
# from . import cy_mesh_point_inside_outside
# mio = cy_mesh_point_inside_outside.MeshPointInsideOutside()


class SliceGeometry():


    def intersection_test(self, stl_path, point):

        ### STL >> [v0, v1, v2]
        meshes = stp.stl2meshes(stl_path)
        print(len(meshes))

        test = mio.poly_mesh_intersection(meshes, point)
        print(test)


    def slice_mesh(self, mesh, volume_size, slice_height, down_sampling):
        
        grid_size_ds = int(volume_size / down_sampling)
        
        new_list = []

        white = tuple([255, 255, 255, 255])
        blank = tuple([0, 0, 0, 255])

        for i in range(grid_size_ds):

            print(i)

            for j in range(grid_size_ds):
                    
                ### Point
                pt = [
                    float(i * down_sampling),
                    float(j * down_sampling),
                    float(slice_height)]
                # print(pt)

                ### Poly-Mesh Point Segment
                intersect_count = mio.poly_mesh_intersection(mesh, pt)
                # print(intersect_count)

                if intersect_count%2 == 1:
                    new_list.append(white)
                else:
                    new_list.append(blank)
                    
        new_tuple = tuple(new_list)

        return new_tuple


    def define_mask(self, stl_path, img_path, volume_size, layer_height, down_sampling):

        ### STL >> [v0, v1, v2]
        meshes = stp.stl2meshes(stl_path)
        print("Mesh Count : {}".format(len(meshes)))

        layer_count = int(volume_size / layer_height)
        print("Layer Count : {}".format(layer_count))

        canvas_size = int(volume_size / down_sampling)
        canvas = imp.create_canvas(canvas_size)
        data_im = canvas.getdata()


        # for i in range(layer_count):
        for i in range(14815, 14816):

            h_slicing = float(i * layer_height)
            h_slicing = 400.0

            print("Processing - Layer : {}".format(i))
            print("Processing - Height : {}".format(h_slicing))

            mask = self.slice_mesh(meshes, volume_size, h_slicing, down_sampling)
            
            canvas.putdata(mask)
            imp.export_image(canvas, img_path)

        return 


    def render():
        pass


