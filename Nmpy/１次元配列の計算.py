"""
リストでは要素ごとの計算を行うには、ループを書いて、要素を１つずつ取り出して足し算を行う必要がありました。
ndarrayではndarray同士の計術演算では、同じ位置にある要素同士を計算します。
"""

import numpy as np

storages = [1, 2, 3, 4]
new_storages = []

for n in storages:
    n += n
    new_storages.append(n)

print(new_storages)

#numpyを使った計算
storages = np.array([1, 2, 3, 4])
storages += storages
print(storages)

