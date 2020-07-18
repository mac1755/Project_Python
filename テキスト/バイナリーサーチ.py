"""
バイナリーサーチを用いて探索をするアルゴリズムプログラムを作成します。
アルゴリズムとは問題を解くための手法の一つです。
データが大きくなるほど、ライナーサーチ（最初から検索する）と比べ、探索にかかる時間が圧倒的に早くなるプログラムです。

①　データの中央値をとる。
②　取り出したデータを目的の物かどうかを比較し、一致する場合は終了。
③　中央値が目的の場合と違う場合は、探索範囲の最小値を中央値に１を足した値にし、
　　大きい場合は探索範囲の最大値を中央値から１を引いた値にする。

（問題）
・関数　binary_searhi の中に、二分探索法を用いてリストの numbers から　target_number を探し出すプログラムを作成してください。
・関数を実行した時に「11は10番目にあります。」と出力させるようにしてください。
・変数 target_number を変更し、自分のプログラムが正しく動いているか確認してください。
・はじめに求める中央値はリストのindexである。
・中央値を求める時、余りが出るではなく切り捨て除算を用いる。
"""

def binary_searhi(numbers, target_number):
    #最小値を求める
    low = 0
    #範囲内の最大値
    hige = len(numbers)
    #目的地を探し出すまでループ
    while low <= hige:
        #中央値を求める
        middel = (low + hige) // 2
        #中央値のnumbersとtarget_numberが等しい場合
        if numbers[middel] == target_number:
            print("{1}は{0}番目にあります。".format(middel, target_number))

            break
        elif numbers[middel] < target_number:
            low = middel +1

        else:
            hige = middel -1


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
target_number = 11

binary_searhi(numbers, target_number)