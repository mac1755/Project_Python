"""
２次元配列は行列に該当します。
np.array(リスト,リスト)　で生成する事ができます。
ndarray配列には shapeという変数があり、ndaraay配列.shape()で各次元ごとの要素を返す事ができる。
nparray配列.reshape(a,b)で指定した引数と同じ型の行列に変換される。
ndarrayの変数を入れずにndarray配列そのものを入れても同じように返す。
"""

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

print(arr.shape)

print(arr.reshape(4,2))
