"""
ndarrayはPythonのリストと同じように代入先の変数の値を変更すると、元のnsarray配列の値も変更されます。
ndarray配列をコピーして２つ別の変数にしたい時は　copy()メソッドを使用します。
このメソッドは　コピーしたい配列.copy()　で使用できます。
"""

import numpy as np

#ndarrayをそのまま別の変数に代入した場合の挙動
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

arr2 = arr1
arr2[0] = 100

#別の変数への変更が元の変数の値も変更している。
print(arr1)

#ndarrayをcopy()を使って別の変数に代入した場合の挙動

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

arr2 = arr1.copy()
arr2[0] = 100

print(arr1)
print(arr2)