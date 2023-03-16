# 1) Найти сумму элементов одномерного массива. Размер произвольный. Элементы вводятся с клавиатуры.

array = []

while True:
    number = input("Number = ")
    if number == '0':
        break
    else:
        array.append(int(number))
print(sum(array))