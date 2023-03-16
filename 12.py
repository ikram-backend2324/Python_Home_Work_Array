# 15) Заполнить массив из 12 элементов случайными числами в интервале [-12..12]
# и выполнить циклический сдвиг ВПРАВО на 4 элемента.

array = []

for repeat in range(10):
    number = input("Number: ")
    if -12 < int(number) < 12:
        array.append(int(number))

# ['1', '2', '3', '-4', '5', '-7', '9', '0', '8', '-1']

for number in array:
    if int(number) < 0:
        array[int(number)] = int(number)*-1
print(array)