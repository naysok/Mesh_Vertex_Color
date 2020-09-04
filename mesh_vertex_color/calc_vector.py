import math

class CalcVector():


    def vector_length(self, vec):
        pass        

    def vector_add(self, va, vb):
        new_vec = [
            float(va[0]) + float(vb[0]),
            float(va[1]) + float(vb[1]),
            float(va[2]) + float(vb[2])]
        return new_vec


    def vector_add_3(self, va, vb, vc):
        vv = self.vector_add(va, vb)
        vvv = self.vector_add(vv, vc)
        return vvv


    def vector_multiplicate(self, vec, value):
        new_vec = [
            float(vec[0]) * value,
            float(vec[1]) * value,
            float(vec[2]) * value]
        return new_vec


    def vector_unitize(self, vec):
        length = math.sqrt(
            math.pow(float(vec[0]), 2) + 
            math.pow(float(vec[1]), 2) + 
            math.pow(float(vec[2]), 2))
        new_vec = self.vector_multiplicate(vec, (1.0 / length))
        return new_vec


    def vector_cross(self, va, vb):
        
        n0 = va[1] * vb[2] - va[2] * vb[1]
        n1 = va[2] * vb[0] - va[0] * vb[2]
        n2 = va[0] * vb[1] - va[1] * vb[0]

        vec = [n0, n1, n2]

        ### Unitizing
        new_vec = self.vector_unitize(vec)

        return new_vec


    def vector_dot(self, va, vb):

        dot_val = va[0] * vb[0] + va[1] * vb[1] + va[2] * vb[2]

        return dot_val


