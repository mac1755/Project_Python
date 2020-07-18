"""
リスト同様、Numpyでもインデックスの参照とスライスをするころができる。
インデックスの参照とスライスの方法はリストと同じです。
１次元配列はスカラー（整数や小数点）となります。
"""
import numpy as np

arr = np.arange(10)
print(arr)

#スライス
arr[0:3] = 1
print(arr)

"""
問題
変数arrの要素のうち、3,4,5だけ出力してください。
変数arrの要素のうち、3,4,5を24に変更してください。
"""

import numpy as np

arr = np.arange(10)
print(arr)

print(arr[3:6])

arr[3:6] = 24
print(arr)

