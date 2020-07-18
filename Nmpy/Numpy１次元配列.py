"""
Numpyには配列を高速で扱うための ndarrayクラスが用意されています。
ndarrayを生成する方法の一つは、Numpyの np.array()関数を用いる方法です。
np.array(リスト)と表記し、リストを与える事で作成します。
"""

import numpy as np

n = np.array([1,2,3])
print(n)

"""
np.arange()関数を用いる方法もあり、np.arange(X)と記載し、等間隔に増減させた要素をX個作成してくれます。
"""

n1 = np.arange(5)
print(n1)

"""
ndarrayクラスは
１次元の場合は　ベクトル
２次元の場合は　行列
３次元の場合は　テンソル
と呼ばれます。
"""
#１次元のnp.array
array_1d = np.array([1,2,3,4,5,6,7,8])

#２次元のnp.array
array_2d = np.array([[1,2,3,4], [5,6,7,8]])

#３次元のnp.array
array_3d = np.array([[1,2], [3,4], [5,6,], [7,8]])

print(array_1d)
print(array_2d)
print(array_3d)
