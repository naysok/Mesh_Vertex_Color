# Mesh_Vertex_Color  


ドット・バイ・ドットのボクセル入稿ができるフルカラー 3D Printing に向けて、メッシュを数理的に解くライブラリ。  


### ToDo  

- [ ] パフォーマンス向上 // Numpy で行列計算、Cupy で GPU 演算。  
- [ ] 距離算出  
- [ ] イージング  


### Index  

- mesh_vertex_color // メッシュを数理的に解くライブラリ  
  - calc_vector.py  
    // 計算   
  - mesh_point_inside_outside.py  
    // ray-triangle を用いたメッシュの内外判定  
  - ray_triangle_intersection.py  
    // Möller-Trumbore intersection algorithm  
  - stl_parser.py  
    // メッシュ面（3頂点）や、ポイントを取り出す  

- rhino_Mesh // gh 上で、格子点からメッシュを書くプログラム  


### Related Projects  

- Contour_Draw_3D  
  [https://github.com/naysok/Contour_Draw_3D](https://github.com/naysok/Contour_Draw_3D)  


### Ref  

- レイと三角形の交差判定（Pheemaの学習帳）  
  [https://pheema.hatenablog.jp/entry/ray-triangle-intersection](https://pheema.hatenablog.jp/entry/ray-triangle-intersection)  

- Möller–Trumbore intersection algorithm（Wikipedia）  
  [https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm)  

- Pythonの計算機イプシロン（Qiita）  
  [https://qiita.com/ikuzak/items/1332625192daab208e22](https://qiita.com/ikuzak/items/1332625192daab208e22)  

- STLファイルフォーマット  
  [https://www.hiramine.com/programming/3dmodelfileformat/stlfileformat.html](https://www.hiramine.com/programming/3dmodelfileformat/stlfileformat.html)

- Stanford Bunny（thingiverse）  
  [https://www.thingiverse.com/thing:3731](https://www.thingiverse.com/thing:3731)  

- Guide to Voxel Printing（GrabCAD）  
  [https://help.grabcad.com/article/230-guide-to-voxel-printing?locale=en&fbclid=IwAR3PvdP71KfqY1herjNa87oGvXnszbsXIcaNfOUYNfbDLn_kIZydNeyYXes](https://help.grabcad.com/article/230-guide-to-voxel-printing?locale=en&fbclid=IwAR3PvdP71KfqY1herjNa87oGvXnszbsXIcaNfOUYNfbDLn_kIZydNeyYXes)  