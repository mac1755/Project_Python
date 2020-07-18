"""
行列計算をするための関数には、２つの行列の行列の積を返すnp.dot(a,b)関数や、
ノルムを返すnp.linalg.norm(a)関数などがあります。
行列の積とは、行列の中にある行ベクトルと列ベクトルとの内積を要素とする行列が新たに作られる事。
np.dot(a,b)  行ベクトルaと列ベクトルbの行列積が出力される。

ノルムとは、ベクトルの長さを返すもので、要素の２乗値を足し合わせて、ルートを被せたもの。
np.linalg.norm(a)  ベクトルa,bのノルムを返す。
"""

import numpy as np

arr = np.arange(9).reshape(3,3)

print(np.dot(arr,arr))

vec = arr.reshape(9)

print(np.linalg.norm(vec))