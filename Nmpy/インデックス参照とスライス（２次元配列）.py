"""
２次元配列の場合、インデックスを１つしか指定しない場合、任意の行を配列で取得できます。
"""
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr[1])
print()
print(arr[0])

"""
個々の要素（スカラー値）にたどり着くには、インデックスを２つ指定する必要があリます。
arr[1][2]又はarr[1,2]で指定します。
arr[1][2]   arr[1]で取り出した配列の3番目の要素にアクセス
arr[1,2]    ２次元配列の軸をそれぞれ指定して要素にアクセス
"""

print(arr[1][2])
print()
print(arr[1,2])

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)

print(arr[0,2])


print(arr[1:, :2])

print(arr[1][0:3])

