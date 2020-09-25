import sys
import numpy as np


#############################################################
###                                                       ###
###   Module for Python3                                  ###
###     * Using Numpy ( + Cupy ? )                        ###
###                                                       ###
#############################################################


class RayTriangleIntersection():

    ### https://pheema.hatenablog.jp/entry/ray-triangle-intersection

    def __init__(self):
        pass


    def calc_intersection(self, o, d, v0, v1, v2):

        e1 = np.subtract(v1, v0)
        e2 = np.subtract(v2, v0)

        ### https://www.it-swarm.dev/ja/python/python-numpy-machine-epsilon/1041749812/
        kEpsilon = np.finfo(float).eps

        alpha = np.cross(d, e2)
        det = np.dot(e1, alpha)

        # print(alpha)
        # print(det)

        ### True = InterSection

        ### Check Parallel
        bool_p = (-kEpsilon > det) or (det > kEpsilon):
        # print("Parallel")
        
        det_inv = 1.0 / det
        r = np.subtract(o, v0)

        ### Check u-Value in the Domain (0 <= u <= 1)
        u = np.dot(alpha, r) * det_inv
        bool_u = (0.0 < u) and (u < 1.0):
        # print("U")

        beta = np.cross(r, e1)

        ### Check v-Value in the Domain (0 <= v <= 1)
        ### and
        ### Check (u + v = 1)
        v = numpy.dot(d, beta) * det_inv
        bool_v = (0.0 < v) and (u + v < 1.0):
        # print("V")
        
        ### Check t_value (t >= 0)
        t = numpy.dot(e2, beta) * det_inv
        bool_t = 0.0 < t:

        ### Intersett : True !!
        # intersect_val = [t, u, v]

        ### Barycenrinc_Coordinate >> XYZ
        ### ((1 - u - v) * v0) + (u * v1) + (v * v2)
        new_v0 = v0 * (1.0 - u - v)
        new_v1 = v1 * u
        new_v2 = v2 * v
        
        intersect_pos = np.add(np.add(new_v0, new_v1), new_v2)
        ray_line = np.subtract(intersect_pos, o)

        ### Check Line-Triangle Intersection
        ### Compare Length, Line-Length / Origin-IntersectPoint-Length
        line_length = np.linalg.norm(d)
        intersect_length = np.linalg.norm(ray_line)

        bool_l = intersect_length < line_length:

        ### Merge Bool
        bool_merged = bool_p & bool_u & bool_v & bool_t & bool_l
        intersect_count = np.nonzero(bool_merged)
        
        # print("Intersection")

        return intersect_count