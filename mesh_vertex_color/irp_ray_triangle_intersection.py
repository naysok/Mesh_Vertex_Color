import sys


from . import irp_calc_vector
reload(irp_calc_vector)
cv = irp_calc_vector.CalcVector()


#############################################################
###                                                       ###
###   Module for ghPython (Rhino / Grasshopper)           ###
###     * Running on IronPython 2                         ###
###     * Not Using Numpy                                 ###
###                                                       ###
#############################################################


class RayTriangleIntersection():

    ### https://pheema.hatenablog.jp/entry/ray-triangle-intersection

    def __init__(self):
        pass
    

    def calc_intersection(self, o, d, v0, v1, v2):

        e1 = cv.vector_subtract(v1, v0)
        e2 = cv.vector_subtract(v2, v0)

        ### https://qiita.com/ikuzak/items/1332625192daab208e22
        kEpsilon = sys.float_info.epsilon

        alpha = cv.vector_cross(d, e2)
        det = cv.vector_dot(e1, alpha)

        # print(alpha)
        # print(det)

        ### (1) Check Parallel
        if (-kEpsilon < det) and (det < kEpsilon):
            # print("Parallel")
            return None
        
        det_inv = 1.0 / det
        r = cv.vector_subtract(o, v0)

        ### (2) Check u-Value in the Domain (0 <= u <= 1)
        u = cv.vector_dot(alpha, r) * det_inv
        if (u < 0.0) or (u > 1.0):
            # print("U")
            return None

        beta = cv.vector_cross(r, e1)

        ### (3) Check v-Value in the Domain (0 <= v <= 1)
        ### and
        ### Check (u + v = 1)
        v = cv.vector_dot(d, beta) * det_inv
        if (v < 0.0) or (u + v > 1.0):
            # print("V")
            return None
        
        ### (4) Check t_value (t >= 0)
        t = cv.vector_dot(e2, beta) * det_inv
        if t < 0.0:
            return None

        ### Intersett : True !!
        # intersect_val = [t, u, v]

        ### Barycenrinc_Coordinate >> XYZ
        ### ((1 - u - v) * v0) + (u * v1) + (v * v2)
        new_v0 = cv.vector_multiplicate(v0, (1.0 - u - v))
        new_v1 = cv.vector_multiplicate(v1, u)
        new_v2 = cv.vector_multiplicate(v2, v)
        
        intersect_pos = cv.vector_add_3(new_v0, new_v1, new_v2)
        ray_line = cv.vector_subtract(intersect_pos, o)

        ### (5) Check Line-Triangle Intersection
        ### Compare Length, Line-Length / Origin-IntersectPoint-Length
        line_length = cv.vector_length(d)
        intersect_length = cv.vector_length(ray_line)
        if intersect_length > line_length:
            return None
        
        # print("Intersection")

        return intersect_pos
