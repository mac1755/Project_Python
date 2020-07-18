"""
Numpyでは　np.randomモジュールで乱数を生成する事ができます。

０以上１未満の一様乱数を生成する　　　np.random.rand()
()の中に整数を入れるとその中に入れた整数の数分の乱数が生成される

関数x以上、y未満の整数をz個生成する　　　np.random.randint(x, y, z)
x以上、y未満の整数を生成する事に注意！
zには(2,3)なども引数に入れる事ができ、その場合は２✖️３の行列を生成する

関数やガウス分布に従う乱数を生成する　　　np.random.normal()

通常これらの関数を使う場合
　　　　　np.random.randint()
と記述するがimportの時に関数名を指定してimportする事で何回も書かなくて済む。
        from numpy.random import randint
と記述する事で　randint()　だけで実行できる。

　　　　「from モジュール名 import そのモジュールの中にある関数名」

"""

import numpy as np

from numpy.random import randint
arr1 = randint(0, 10, (5,2))
print(arr1)


arr2 = np.random.rand(3)
print(arr2)
