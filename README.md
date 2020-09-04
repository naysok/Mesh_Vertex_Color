# Mesh_Vertex_Color  


ドット・バイ・ドットのボクセル入稿ができるフルカラー 3D Printing に向けて、メッシュを数理的に解くライブラリ。  


### ToDo  

- STL パーサーの実装  
- PIL を用いて画像に吐き出す  
- 距離算出  
- イージング  
- パフォーマンステスト  


### Index  

- mesh_vertex_color // メッシュを数理的に解くライブラリ  
  - calc_vector.py  
    // 計算   
  - mesh_point_inside_outside.py
    // ray-triangle を用いた内外判定 
  - ray_triangle_intersection.py
    // Möller-Trumbore intersection algorithm で実装した ray-triangle
  - stl2mesh.py
    // STL パーサー。とりあえずアスキーだけで。

- rhino_Mesh // gh 上で、格子点からメッシュを書くプログラム  


### Ref  

- レイと三角形の交差判定（Pheemaの学習帳）  
  [https://pheema.hatenablog.jp/entry/ray-triangle-intersection](https://pheema.hatenablog.jp/entry/ray-triangle-intersection)  

- Möller–Trumbore intersection algorithm（Wikipedia）  
  [https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm)  

- Pythonの計算機イプシロン（Qiita）  
  [https://qiita.com/ikuzak/items/1332625192daab208e22](https://qiita.com/ikuzak/items/1332625192daab208e22)