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
        
        # det = np.dot(e1, alpha)
        det = np.sum(e1 * alpha, axis=1)

        # print("e1.shape : {}".format(e1.shape))
        # print("e2.shape : {}".format(e2.shape))
        # print("alpha.shape : {}".format(alpha.shape))
        # print("det.shape : {}".format(det.shape))

        # intersect_count = np.count_nonzero(det)
    

        ### True = InterSection

        ### (1) Check Parallel
        bool_p = (-kEpsilon > det) | (det > kEpsilon)

        ### Remove (1)
        v0 = v0[bool_p]
        v1 = v1[bool_p]
        v2 = v2[bool_p]
        e1 = e1[bool_p]
        e2 = e2[bool_p]
        alpha = alpha[bool_p]
        det = det[bool_p]
        # print("det.shape (1) : {}".format(det.shape))
        
        
        det_inv = 1.0 / det
        r = np.subtract(o, v0)

        ### (2) Check u-Value in the Domain (0 <= u <= 1)
        # u = np.dot(alpha, r) * det_inv
        u = np.sum(alpha * r, axis=1) * det_inv
        bool_u = (0.0 < u) & (u < 1.0)

        ### Remove (2)
        v0 = v0[bool_u]
        v1 = v1[bool_u]
        v2 = v2[bool_u]
        e1 = e1[bool_u]
        e2 = e2[bool_u]
        alpha = alpha[bool_u]
        r = r[bool_u]
        u = u[bool_u]
        det = det[bool_u]
        det_inv = det_inv[bool_u]
        # print("det.shape (2) : {}".format(det.shape))


        beta = np.cross(r, e1)

        ### (3) Check v-Value in the Domain (0 <= v <= 1)
        ### and
        ### Check (u + v = 1)
        # v = np.dot(d, beta) * det_inv
        v = np.sum(d * beta, axis=1) * det_inv
        bool_v = (0.0 < v) & (u + v < 1.0)
        
        ### Remove (3)
        v0 = v0[bool_v]
        v1 = v1[bool_v]
        v2 = v2[bool_v]
        e1 = e1[bool_v]
        e2 = e2[bool_v]
        alpha = alpha[bool_v]
        beta = beta[bool_v]
        r = r[bool_v]
        u = u[bool_v]
        v = v[bool_v]
        det = det[bool_v]
        det_inv = det_inv[bool_v]
        # print("det.shape (3) : {}".format(det.shape))

        
        ### (4) Check t_value (t >= 0)
        # t = np.dot(e2, beta) * det_inv
        t = np.sum(e2 * beta, axis=1) * det_inv
        bool_t = 0.0 < t

        ### Remove (4)
        v0 = v0[bool_t]
        v1 = v1[bool_t]
        v2 = v2[bool_t]
        e1 = e1[bool_t]
        e2 = e2[bool_t]
        alpha = alpha[bool_t]
        beta = beta[bool_t]
        r = r[bool_t]
        t = t[bool_t]
        u = u[bool_t]
        v = v[bool_t]
        det = det[bool_t]
        det_inv = det_inv[bool_t]
        # print("det.shape (4) : {}".format(det.shape))

        ### Intersett : True !!
        # intersect_val = [t, u, v]

        ### Barycenrinc_Coordinate >> XYZ
        ### ((1 - u - v) * v0) + (u * v1) + (v * v2)

        new_amp = 1.0 - u - v        
        new_v0 = np.multiply(v0, new_amp[:, np.newaxis])
        new_v1 = np.multiply(v1, u[:, np.newaxis])
        new_v2 = np.multiply(v2, v[:, np.newaxis])
        
        intersect_pos = np.add(np.add(new_v0, new_v1), new_v2)
        ray_line = np.subtract(intersect_pos, o)
        # print("ray_line.shape : {}".format(ray_line.shape))

        ### (5) Check Line-Triangle Intersection
        ### Compare Length, Line-Length / Origin-IntersectPoint-Length
        line_length = np.linalg.norm(d)
        intersect_length = np.linalg.norm(ray_line, axis=1)
        # print("line_len : {}".format(line_length))
        # print("inter_len : {}".format(intersect_length))
        # print("inter_len.shape : {}".format(intersect_length.shape))

        bool_l = intersect_length < line_length
        # print(bool_l)

        intersect_count = np.count_nonzero(bool_l)
        
        return intersect_count