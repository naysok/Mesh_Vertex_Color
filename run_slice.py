import time
import numba

from mesh_vertex_color import slice_geometry

sg = slice_geometry.SliceGeometry()


prj_path = "C:\\Users\\ysoky\\Documents\\Mesh_Vertex_Color\\"
stl_path = prj_path + "_stl_\\bunny-flatfoot_fixed_light.stl"

VOLUME_SIZE = 600.0
LAYER_HEIGHT = 0.027
DOWN_SAMPLING = 10

img_path = prj_path + "_images_\\test.png"


time_0 = time.time()


sg.define_mask(stl_path, img_path, VOLUME_SIZE, LAYER_HEIGHT, DOWN_SAMPLING)


# point_test = [400, 400, 200]
# sg.intersection_test(stl_path, point_test)


time_1 = time.time()


time_01 = time_1 - time_0
print("Time_01 : {}Sec".format(time_01))