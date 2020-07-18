#formatは　{} の中に任意の値を入れることができる。
print("私は{}歳です。".format(20))

# %を文字列の中に記述することで、文字列の後ろ側に置かれたオブジェクトを引き渡す事ができる。

pai = 3.141592
# %d  整数で表示
# %f  小数で表示
# %.f2  小数第２位まで表示
# %s  文字列として表示

print("円周率は、%f" %pai)
print("円周率は、 %.2f" %pai)

def dmi(height, weight):
    return weight / height ** 2

print("dmiは %.4f です。" %dmi(1.65, 65))

#問題
#objectの中から charavter を含む要素数を数える関数を作ってください。
#引数に object,character をとる関数、check_character を作成してください。
#戻り値として count() メソッドで文字列やリストと個数を調べたい要素を入力してください。

def check_character(object, charavter):
    return object.count(charavter)

print(check_character([1,2,3,4,5,6,4,3,2,1,3,3,4,3],3))
print(check_character("asdgaoirnoiafvnwoeo", "d"))
