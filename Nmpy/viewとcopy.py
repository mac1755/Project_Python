"""
Pythonのリストとndarrayの相違点は、ndarrayのスライスは配列のコピーではなく、viewである事。
view は元の配列と同じデータを指しています。
ndarrayのスライスの変更は、オリジナルのndarrayを変更する事になります。
スライスをコピーとして扱いたい場合は、 arr[:].copy()  と書きます。
"""

import numpy as np

#Pythonのリストでスライスを用いた場合
arr_list = [x for x in range(10)]
print("リスト型データです。")
print(arr_list)

print()
arr_list_copy = arr_list[:]
arr_list_copy[0] = 100

print("リストのスライスではコピーが作られるので、arr_listにはarr_list_copyの変更が反映されません。")
print(arr_list)
print()

#numpyのndarrayでスライスを用いた場合の挙動
arr_Numpy = np.arange(10)
print("Numpyでのndarrayデータです。")
print(arr_Numpy)
print()

arr_Numpy_view = arr_Numpy[:]
arr_Numpy_view[0] = 1200

print("Numpyのスライスではview(データが格納されている場所)が代入されているので、arr_Numpy_viewの変更がarr_Numpyに反映されます。")
print(arr_Numpy)
print()

#numpyでndarrayにcopu()を用いた場合の挙動
arr_Numpy = np.arange(10)
print("Numpyのndarrayでcopy()を用いた場合の挙動です。")
print(arr_Numpy)
print()

arr_Numpy_copy = arr_Numpy[:].copy()
arr_Numpy_copy[0] = 1200
print("copy()を用いた場合は、コピーが生成されるのでarr_Numpy_copyはarr_Numpyに影響を与えません。")
print(arr_Numpy)
