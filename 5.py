# 5)  В заданном одномерном  массиве, состоящем из n  целых чисел, подсчитать количество четных элементов.

array = []
even_Numbers = []

while True:
    number = input("Number = ")
    if number == '0':
        break
    else:
        array.append(number)
for i in array:
    if int(i) % 2 == 0:
        even_Numbers.append(i)

print(len(even_Numbers))