# 6) Массив А вводится с клавиатуры.
# Сформировать новый массив В, состоящий из четных элементов массива А.
# Элементы вводятся с клавиатуры. Размер n.

A = []
B = []
N = int(input("N = "))
for number in range(N+1):
    A.append(number)
for i in A:
    if int(i) % 2 == 0:
        B.append(i)
print(A)
print(B)
