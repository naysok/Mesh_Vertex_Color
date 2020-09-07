import math
import time

import numpy as np


from mesh_vertex_color import ray_triangle_intersection
rt = ray_triangle_intersection.RayTriangleIntersection()

from mesh_vertex_color import slice_geometry
sg = slice_geometry.SliceGeometry()


dir_path = "C:\\Users\\ysoky\\Documents\\Mesh_Vertex_Color\\"
stl_path = dir_path + "_stl_\\bunny-flatfoot_fixed_light.stl"
prj_path = dir_path + "_images_\\test\\"


### Size (mm)
VOLUME_SIZE = 50.8
LAYER_HEIGHT = 0.027


### Dot Size (mm)
_INCH = 25.4
GRID_SIZE = _INCH / 300.0
# print(GRID_SIZE)

### Down Sampling
DOWN_SAMPLING_XY = 2
DOWN_SAMPLING_Z = 2



img_path = prj_path + "test_0.png"


# time_0 = time.time()



# sg.define_mask(stl_path, img_path, VOLUME_SIZE, LAYER_HEIGHT, DOWN_SAMPLING)


# point_test = [400, 400, 200]
# sg.intersection_test(stl_path, point_test)
### 0.06806588172912598Sec




time_0 = time.time()

time_1 = time.time()

time_2 = time.time()


print("Time_01 : {}Sec".format(time_1 - time_0))
print("Time_12 : {}Sec".format(time_2 - time_1))
