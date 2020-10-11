import math

class CalcVector():


    def vector_length(self, vec):
        
        length = math.sqrt(
            math.pow(float(vec[0]), 2) + 
            math.pow(float(vec[1]), 2) + 
            math.pow(float(vec[2]), 2))
        
        return length


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

    
    def vector_subtract(self, va, vb):

        new_vec = [
            float(va[0]) - float(vb[0]),
            float(va[1]) - float(vb[1]),
            float(va[2]) - float(vb[2])]
        
        return new_vec


    def vector_multiplicate(self, vec, value):

        new_vec = [
            float(vec[0]) * value,
            float(vec[1]) * value,
            float(vec[2]) * value]

        return new_vec


    def vector_unitize(self, vec):

        length = self.vector_length(vec)
        new_vec = self.vector_multiplicate(vec, (1.0 / length))

        return new_vec


    def vector_cross(self, va, vb):

        n0 = (float(va[1]) * float(vb[2])) - (float(va[2]) * float(vb[1]))
        n1 = (float(va[2]) * float(vb[0])) - (float(va[0]) * float(vb[2]))
        n2 = (float(va[0]) * float(vb[1])) - (float(va[1]) * float(vb[0]))

        vec = [n0, n1, n2]

        return vec


    def vector_dot(self, va, vb):

        dot_val = (float(va[0]) * float(vb[0])) + (float(va[1]) * float(vb[1])) + (float(va[2]) * float(vb[2]))

        return dot_val


