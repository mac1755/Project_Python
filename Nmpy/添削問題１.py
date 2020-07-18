"""
・各要素が０〜３０の整数の行列(5✖️３)を変数arrに代入して下さい。
・変数arrを転置して下さい。
・変数arrの２、３、４列のみの行列（３✖️３）を変数arr1に代入して下さい。
・変数arr1を行でソートして下さい。
・各列の平均を出力してください。
"""

import numpy as np

np.random.seed(100)

#各要素が０〜３０の整数の行列（５✖️３）を変数arrに代入してください。
arr = np.random.randint(0,31,(5,3))
print(arr)

#変数arrを転置してください。
arr = arr.T
print(arr)

#変数arrの２、３、４列のみの行列（３✖️３）を変数arr1に代入してください。
arr1 = arr[:,1:4]
print(arr1)

#変数arr1を行でソートしてください。
arr1.sort(0)
print(arr1)

#各列の平均を出力してください。
print(np.average(arr1, axis=0))