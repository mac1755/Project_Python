"""
統計関数とは　　ndarray配列全体、特定の軸を中心とした数学的な処理を行う関数またはメソッド
sum()メソッド　　配列の和を返す。
mean()メソッド　配列要素の平均を返す
np.average()  mean()メソッド同じ
np.max()メソッド　　最大値を返す
np.min()メソッド　　最小値を返す
np.argmax()メソッド　最大値のインデックス番号を返す
np.argmin()メソッド　最小値のインデックス番号を返す

（データのばらつきを示す指標）
np.std()メソッド　　標準偏差
np.var()メソッド　　分散

sum()メソッドでaxisで指定する事によりどの軸を中心に処理するかを決める事ができるように、mean()メソッドでも同じような事ができる。
argmax()やargmin()でaxisを指定すると指定された軸を元に最大または最小のインデックスを返す。

列ごとに処理を行う軸が、　axis=0
行ごとに処理を行う軸が、　axis=1
"""

import numpy as np

arr = np.arange(15).reshape(3,5)

#変数arrの列ごとの平均
print(np.mean(arr, axis=0))

#変数arrの行の合計
print(arr.sum(axis=1))

#変数arrの最小値
print(np.min(arr))

#変数arrのそれぞれの列の最大値のインデックス番号
print(np.argmax(arr,axis=0))

