# 2)  Найти сумму элементов массива с четными номерами, содержащего N элементов. Элементы вводятся с клавиатуры.

array = []
N = int(input("N = "))
for i in range(N):
    if i % 2 == 0:
        array.append(int(i))
print(sum(array))
