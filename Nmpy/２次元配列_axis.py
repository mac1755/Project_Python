"""
２次元配列からはaxisという概念が重要になってきます。
axisとは座標軸のような物です。
Numpyの関数の引数として使われる場面が多々あります。
　列ごとに処理を行う軸がaxis=0,  行ごとに処理を行う軸がaxis=1
ndarray配列のsum()メソッドで考えます。
"""

import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

"""
sum()メソッドに何も引数を与えずに実行すると、単純な合計がスカラー値として返ってきます。
sum()メソッドの引数に axis=0　を与えて実行すると、縦に足し算が行われて要素が３つの１次元配列で返ってきます。
sum()メソッドの引数に　axis=1 を与えて実行すると、横に足し算が行われて要素が２つの１次元配列で返ってきます。
"""

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(arr.sum(axis=0))
print(arr.sum(axis=1))
