"""
ブールインデックス参照とは　[] の中に論理値（True/Fales）の配列を用いて要素を取り出す方法
arr[ndarrayの論理値の配列]と表記すると、論理値配列のTrueに該当する箇所の要素のndarrayを作成して返す。
"""

import numpy as np

arr = np.array([2, 4, 6, 7])
print(arr[np.array([True, True, True, False])])


#3で割った時の余りが１の要素をTrueとして返し、3で割った時の要素を出力する。
arr = np.array([2, 4, 6, 7])
print(arr[arr % 3 == 1])


"""
問題
変数arrの各要素が２で割り切れるかどうかを示す真偽値の配列を出力してください。
変数arrの各要素のうち、２で割り切れる要素の配列を出力してください。
"""

import numpy as np

arr = np.array([2, 3, 4, 5, 6, 7])

print(arr % 2 == 0)
print(arr[arr % 2 == 0])


