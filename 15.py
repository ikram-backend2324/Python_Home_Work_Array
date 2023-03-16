# 18) Найти номер и значение первого положительного элемента массива.

array = []
while True:
    number = input("Number = ")
    if number == '0':
        break
    else:
        array.append(int(number))
for number in array:
    if number > 0:
        print(number)
        print(array.index(number))
        break
