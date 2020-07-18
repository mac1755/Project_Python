"""
numpyとは、Pythonでベクトルや行列計算を高速に行う事に特化したライブラリーです。
ライブラリーとは外部から取り込むPythonコードの塊です。
ライブラリーの中にはたくさんのモジュールが入っており、モジュールとはたくさんの関数でまとまっている塊です。
以下でnumpyの高速な処理を記述します。
"""

import numpy as np
import time
from numpy.random import rand

#行、列の大きさ
N = 150

#行列を初期化します。
matA = np.array(rand(N,N))
matB = np.array(rand(N,N))
matC = np.array([[0] * N for _ in range(N)])

#Pythonのリストを使って計算します。

#開始時間を取得します。
start = time.time()

#for文を使って行列の掛け算を実行します。
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("Python機能のみでの計算結果: %.2f[sec]" % float(time.time() - start))



#numpyによる計算
start = time.time()

#numpyを使って行列の計算をします。
matC = np.dot(matA, matB)

#小数第２位で打ち切っているので、Numpyは0.00[esc]と表示される場合であっても、０ではありません。
print("Numpyを使った場合の計算結果: %.2f[esc]" % float(time.time() - start))
