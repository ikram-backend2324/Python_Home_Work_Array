# Сложный

# 14) Заполнить массив из 10 элементов случайными
# числами в интервале [-10..10] и сделать реверс отдельно для 1-ой и 2-ой половин массива.

first_Array = []

for repeat in range(10):
    number = input("Number: ")
    if -10 < int(number) < 10:
        first_Array.append(number)

second_Array = first_Array.copy()
second_Array.reverse()
print(first_Array)
print(second_Array)
