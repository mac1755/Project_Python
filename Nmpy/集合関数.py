"""
集合関数とは数学の集合関数を行う関数で、１次元配列のみを対象としている。
重複を取り除きそれをソートした結果を返す　　　np.unique()
配列xとyのうち少なくとも一方に存在する要素を取り出しソートする　　　np.union1d(x,y)  (和集合)
配列xとyの共通する要素を取り出しソートする　　np.intersect1d(x,y)  （積集合）
配列xと配列yの共通する要素を配列xから取り除きソートする　　　np.setdiff1d(x,y)　　（差集合）　
"""

"""
問題
・np.unique()関数を用いて、変数arr１の重複をなくした配列を変数 new_arr1 に代入してください。
・変数new_arr1と変数arr2の和集合を出力してください。
・変数new_arr1と変数arr2の積集合を出力してください。
・変数new_arr1から変数arr2を引いた差集合を出力してください。
"""
import numpy as np

arr1 = np.array([2, 5, 7, 9, 5, 2])
arr2 = np.array([2, 5, 8, 3, 1])

#np.unique()関数を用いて重複をなくした配列を変数new_arr1に代入してください。
new_arr1 = np.unique(arr1)
print(new_arr1)

#変数new_arr1と変数arr2の和集合を出力してください。
print(np.union1d(new_arr1, arr2))
#変数new_arr1と変数arr2の積集合を出力してください。
print(np.intersect1d(new_arr1, arr2))
#変数new_arr1から変数arr2を引いた差集合を出力してください。
print(np.setdiff1d(new_arr1, arr2))

