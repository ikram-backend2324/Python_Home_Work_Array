# 8) Создайте массив из 15 целочисленных элементов и определите среди них минимальное значение.

array = []
for repeat in range(15):
    number = input("Number: ")
    array.append(number)

print(min(array))