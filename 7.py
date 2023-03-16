# 7) Введите с клавиатуры в массив пять целочисленных значений. Выведите их в одну строку через запятую.
# Получите для массива среднее арифметическое.

array = []
summa = 0
for repeat in range(5):
    number = input("Number = ")
    array.append(number)
for number in array:
    summa += int(number)
print(summa / int(len(array)))