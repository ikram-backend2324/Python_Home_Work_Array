# 4)  В заданном одномерном  массиве, состоящем из n  целых чисел, подсчитать количество нулей.

array = []

number = str(input("Number = "))
for i in number:
    if i == '0':
        array.append(i)
print(len(array))