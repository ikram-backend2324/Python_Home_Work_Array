# # 16) Вывести элементы числового массива, которые больше, чем элементы, стоящие перед ними.

array = []

for repeat in range(15):
    array.append(int(repeat))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

index1 = 0
index2 = 1

for i in array:
    if array[index1] < array[index2]:
        del array[index1]
        index1 += 2
        index2 += 2

# Traceback (most recent call last):
#   File "C:\Python\Python Array_hard\13.py", line 14, in <module>
#     if array[index1] < array[index2]:
# IndexError: list index out of range