"""
・変数arr同士を足した物を出力してください。
・変数arr同士を引いた物を出力してください。
・変数arrの３乗を出力してください。
・１を変数arrで割った値を出力してください。
・出力はprint()関数を用いてください。
"""

import numpy as np

arr = np.array([2, 5, 3, 4, 8])

print(arr + arr)

print(arr - arr)

print(arr ** 3)

print(1 / arr)
