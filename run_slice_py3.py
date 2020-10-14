import math
import time

import numpy as np


### Python3

from mesh_vertex_color import np_slice_geometry
sg = np_slice_geometry.SliceGeometry()


prj_name = "test"


### WINDOWS 10
# dir_path = "C:\\Users\\ysoky\\Documents\\Mesh_Vertex_Color\\"
# prj_path = dir_path + "_images_\\" + prj_name
# stl_path = dir_path + "_stl_\\bunny-flatfoot_fixed_light.stl"


### MBP
dir_path = "/Users/yoshionao_mbp/Documents/Mesh_Vertex_Color/"
prj_path = dir_path + "_images_/" + prj_name
stl_path = dir_path + "_stl_/bunny-flatfoot_fixed_light.stl"


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


##########


time_0 = time.time()


############################## Test ##############################

### Inside/Outside

point_test = [300, 300, 300]

### Re-Size Point
pt = [
    float(point_test[0] * GRID_SIZE),
    float(point_test[1] * GRID_SIZE),
    float(point_test[2] * GRID_SIZE)]

print("Point : {}, {}, {}".format(pt[0], pt[1], pt[2]))

sg.intersection_test(stl_path, pt)
### 0.06806588172912598Sec

############################## Test ##############################



# sg.define_mask(stl_path, img_path, VOLUME_SIZE, LAYER_HEIGHT, DOWN_SAMPLING)





time_1 = time.time()

print("Time_01 : {}Sec".format(time_1 - time_0))
