# 9) Найти количество четных элементов одномерного массива.

even_Numbers = []
while True:
    number = input("Numer: ")
    if number == '0':
        break
    else:
        even_Numbers.append(number)
for number in even_Numbers:
    if int(number) % 2 == 0:
        print(number, end=", ")
