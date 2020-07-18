"""
ndarrayもリスト同様に、sort()メソッドでソートする事ができる。
２次元配列の場合、０を引数にすると列単位で要素がソートされ、
１を引数にすると行単位で要素がソートされる。
np.sort()関数　　ソートした配列のコピーを返す関数
argsort()メソッド　ソート後の配列のインデックスを返す。
"""

import numpy as np

#ソート後のインデックス番号を返す
arr = np.array([15, 30, 5])
print("[15, 30, 5]をソートしたインデックス番号を出力する")
print(arr.argsort())

#ソートは順番を並び替える
arr1 = np.sort(arr)
print(arr1)

"""
問題
変数arrをargsort()メソッドでソートして出力してください。
変数arrをnp.sort()関数でソートして出力してください。
変数arrをsort()メソッドにより行でソートしてください。
"""
arr = np.array([[8,4,2],[3,5,1]])

print(arr.argsort())

print(np.sort(arr))

arr.sort(1)
print(arr)