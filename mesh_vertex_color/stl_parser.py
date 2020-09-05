

class StlParser():


    def file_open(self, file_path):

        with open(file_path) as f:
            l = f.readlines()
        
        return l


    def format_stl_vertex_to_str(self, stl_vertex):

        ### "vertex xx yy zz" >> "xx,yy,zz"
        
        stl_vertex_rm = stl_vertex.replace("\n", "")
        stl_vertex_sp = stl_vertex_rm.split(" ")

        x = float(stl_vertex_sp[-3])
        y = float(stl_vertex_sp[-2])
        z = float(stl_vertex_sp[-1])

        new_str = "{},{},{}".format(x, y, z)
    
        return new_str
    

    def xyz_str_to_list(self, xyz_str):

        ### "xx,yy,zz" >> [xx, yy, zz]
        x, y, z = xyz_str.split(",")
        xx = float(x)
        yy = float(y)
        zz = float(z)

        return [xx, yy, zz]


    def format_stl_vertex_to_list(self, stl_vertex):

        ### "vertex xx yy zz" >> [xx, yy, zz]
        
        stl_vertex_rm = stl_vertex.replace("\n", "")
        stl_vertex_sp = stl_vertex_rm.split(" ")

        new_list = []

        new_list.append(float(stl_vertex_sp[-3]))
        new_list.append(float(stl_vertex_sp[-2]))
        new_list.append(float(stl_vertex_sp[-1]))
    
        return new_list


    def stl2points(self, file_path):
        
        lines = self.file_open(file_path)
        # print(len(lines))

        DEFINE_FACE_LINES = 7

        i = 0

        stl_points = []

        ### STL Parse
        while (i * DEFINE_FACE_LINES) < len(lines) - 2:

            idx = (i * DEFINE_FACE_LINES) + 1
            
            ### Get String
            # face_start_nrl_vec = lines[idx]
            # loop_start = lines[idx + 1]
            v0 = str(lines[idx + 2])
            v1 = lines[idx + 3]
            v2 = lines[idx + 4]
            # loop_end = lines[idx + 5]
            # face_end = lines[idx + 6]

            ### Format
            ### "vertex xx yy zz" >> "xx,yy,zz"
            v0_list = self.format_stl_vertex_to_str(v0)
            v1_list = self.format_stl_vertex_to_str(v1)
            v2_list = self.format_stl_vertex_to_str(v2)

            stl_points.append(v0_list)
            stl_points.append(v1_list)
            stl_points.append(v2_list)

            i += 1
        
        ### Remove Duplicate Elements
        ### List >> Set
        stl_points_set = set(stl_points)
        ### Set >> List
        stl_points_list = list(stl_points_set)

        ### Format
        ### "xx,yy,zz" >> [xx, yy, zz]
        new_list = []

        for j in range(len(stl_points_list)):
            l = self.xyz_str_to_list(stl_points_list[j])
            new_list.append(l)

        return new_list


    def stl2meshes(self, file_path):

        lines = self.file_open(file_path)
        # print(len(lines))

        DEFINE_FACE_LINES = 7

        i = 0

        stl_meshes = []

        ### STL Parse
        while (i * DEFINE_FACE_LINES) < len(lines) - 2:

            idx = (i * DEFINE_FACE_LINES) + 1
            
            ### Get String
            # face_start_nrl_vec = lines[idx]
            # loop_start = lines[idx + 1]
            v0 = str(lines[idx + 2])
            v1 = lines[idx + 3]
            v2 = lines[idx + 4]
            # loop_end = lines[idx + 5]
            # face_end = lines[idx + 6]

            ### Format
            ### "vertex xx yy zz" >> [xx, yy, zz]
            v0_list = self.format_stl_vertex_to_list(v0)
            v1_list = self.format_stl_vertex_to_list(v1)
            v2_list = self.format_stl_vertex_to_list(v2)

            ### Define Face
            face_list = []

            face_list.append(v0_list)
            face_list.append(v1_list)
            face_list.append(v2_list)

            stl_meshes.append(face_list)

            i += 1

        return stl_meshes



