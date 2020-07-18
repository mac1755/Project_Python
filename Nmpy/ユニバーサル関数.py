"""
ユニバーサル関数とはndarray配列の各要素に対して演算した結果を返す関数。
要素ごとの演算なので多次元配列の演算でも用いる事ができる。

引数が１つの時
要素の絶対値を返す　　np.abs()
要素のe(自然対数の底)のべき乗を返す　　np.exp()
関数や要素の平方根を返す　　　np.sqrt()

引数が２つの時
要素同士の和を返す　　　np.add()
関数、要素同士の差を返す　　　np.subtract()
関数や要素同士の最大値を格納した配列を返す　　np.maximum()
"""

import numpy as np

arr = np.array([4, -4, 16, -4, 20])
print(arr)

arr_abs = np.abs(arr)
print(arr_abs)

print(np.exp(arr_abs))
print(np.sqrt(arr_abs))
