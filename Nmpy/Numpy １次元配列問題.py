"""
変数 storages からndarray配列を生成し、変数 np_storagesに代入してください。
変数 np_storagesの型を出力してください。
"""
import numpy as np

storages = [24, 3, 4, 23, 10, 12]
print(storages)

np_storages = np.array(storages)

print(np_storages)
print(type(np_storages))

