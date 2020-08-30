import math
import rhinoscriptsyntax as rs


class Operate_Mesh():


    def define_mesh_points(self, num):
        
       pts = []
       
       for i in xrange(num):
           for j in xrange(num):
               pts.append(rs.AddPoint(i, j ,0))
       
       return pts


    def define_mesh_points_triangle(self, num):
        
        pts = []
        
        for i in xrange(num):
            for j in xrange(num):
                
                yy = j * (math.sin((1.0 / 3.0) * math.pi))

                if j%2 == 0:
                     xx = i
                else:
                     xx = i + (math.cos((1.0 / 3.0) * math.pi))
                
                pts.append(rs.AddPoint(xx, yy ,0))
        
        return pts


    def define_mesh_faces(self, num):
        
        faces = []

        for i in xrange(num - 1):
            for j in xrange(num - 1):
                a = i * num + j
                b = (i+1) * num + j
                c = (i+1) * num + (j+1)
                d = i * num + (j+1)

                if j%2 == 0:
                    face_id_a = "{};{};{};".format(a, b, d)
                    face_str_a = "T{" + face_id_a +"}"
                    
                    face_id_b = "{};{};{};".format(b, c, d)
                    face_str_b = "T{" + face_id_b +"}"
                    
                    faces.append(face_str_a)
                    faces.append(face_str_b)
                    
                else:
                    face_id_a = "{};{};{};".format(a, b, c)
                    face_str_a = "T{" + face_id_a +"}"
                    
                    face_id_b = "{};{};{};".format(a, c, d)
                    face_str_b = "T{" + face_id_b +"}"
                    
                    faces.append(face_str_a)
                    faces.append(face_str_b)
        
        return faces