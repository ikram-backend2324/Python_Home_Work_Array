# 10) Вычислить сумму четных элементов одномерного массива до первого встреченного нулевого элемента.

array = []
even_Numbers = 0

while True:
    number = input("Numer: ")
    if number == '0':
        break
    else:
        array.append(number)
for number in array:
    if number == '0':
        break
    else:
        if int(number) % 2 == 0:
            even_Numbers += int(number)
print(even_Numbers)