# 3) Найти наименьший элемент одномерного массива, состоящего из n элементов. Элементы вводятся с клавиатуры.

array = []
while True:
    n = input("N = ")
    if n == "0":
        break
    else:
        array.append(int(n))
print(min(array))
