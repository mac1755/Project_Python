"""
行列では行と列を入れ替えることを転換といいます。
転置行列は、行列の内積の計算などで使う場合があります。
ndarrayを転置するには、np.transpose() 関数を用いる方法と　.T を用いる方法があります。
"""

#変数arrを転置させ出力する
import numpy as np

arr = np.arange(10).reshape(2,5)
print(arr)

print(arr.T)
print(np.transpose(arr))

