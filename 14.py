# 17) Все элементы массива поделить на значение наибольшего элемента этого массива.

array = []

while True:
    number = input("Number = ")
    if number == '0':
        break
    else:
        array.append(number)
max_Number = max(array)
indexMaxNumber = array.index(max_Number)
o_MaxNumber = array.pop(indexMaxNumber)
Summa = 0

for i in array:
    Summa += int(i)

print(float(int(o_MaxNumber)/Summa))

