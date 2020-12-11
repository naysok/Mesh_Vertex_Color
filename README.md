切断面を画像解像度で、全ピクセルへメッシュの内外判定をかけてというダメダメ設計なので凍結。新たに書き直します。（2020/12/11）  


# ~~Mesh_Vertex_Color~~  


~~ドット・バイ・ドットのボクセル入稿ができるフルカラー 3D Printing に向けて、メッシュを数理的に解くライブラリ。~~  

~~このライブラリで生成した連番画像から 3D 描画は、3D プリントデータへの変換ソフトではできるが、適当なソフトウェアでは難しい。これだと不便なので擬似的にレンダリングを行うライブラリを書いた。~~  


### ToDo  

- [ ] マスク等パフォーマンス向上 // Numpy で行列計算（ + Cupy で GPU 演算）  
- [ ] メッシュ頂点からの距離算出  
- [ ] 入力点群からの距離算出  
- [ ] イージング  


### Index  

- mesh_vertex_color // メッシュを数理的に解くライブラリ（IronPython2 / CPython3）  
  
  - image_processing.py  
    // 画像処理全般  

  - irp_calc_vector.py  
    // 計算 （for IronPython）  

  - irp_mesh_point_inside_outside.py  
    // ray-triangle を用いたメッシュの内外判定 （for IronPython）  
  
  - irp_ay_triangle_intersection.py  
    // Möller-Trumbore Intersection Algorithm （for IronPython） 

  - irp_slice_geometry.py  
    // ジオメトリ処理全般 （for IronPython）  
  
  - np_mesh_point_inside_outside.py  
    // ray-triangle を用いたメッシュの内外判定  
  
  - np_ray_triangle_intersection.py  
    // Möller-Trumbore Intersection Algorithm  
  
  - np_slice_geometry.py  
    // ジオメトリ処理全般  
  
  - stl_parser.py  
    // メッシュ面（3頂点）や、ポイントを取り出す  

- rhino_Mesh // gh 上で、格子点からメッシュを書くプログラム  


### Related Projects  

- Contour_Draw_3D  
  // 3D ジオメトリを輪切りして切り出した断面の連番画像から、擬似的に 3D ジオメトリを描画するライブラリ  
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

  - Vectorized way of calculating row-wise dot product two matrices with Scipy（Stackoverrun）  
  [https://stackoverrun.com/ja/q/4238423](https://stackoverrun.com/ja/q/4238423)  