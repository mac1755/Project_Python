"""
ブロードキャスト　　　２つのndraay同士の演算時にサイズの小さい配列の行と列を自動で大きい配列に合わせます。
２つの配列の行が一致しない時は行の少ない方が多い方の数に合わせ、足りない部分を既存の行からコピーします。
全ての要素に同じ処理をする時にブロードキャストを使います。
"""

import numpy as np

x = np.arange(6).reshape(2,3)
print(x * 2)

"""
問題
0から14の整数値を持つ１次ndarray配列yを用いて、配列xの各要素から列のインデックス番号を引いて下さい。
ただし、左から最初の列を０とします。
"""

x = np.arange(15).reshape(3,5)

y = np.array([np.arange(5)])
print(y)

z = x -y
print(z)
