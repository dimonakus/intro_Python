# Задача 32: Определить индексы элементов массива (списка),``
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

def arr(a):
    numb = []
    for i in range(a):
        numb.append(random.randint(-20, 50))
    return numb

def find_indx(numb, minval, maxval):
    indx = []
    for i in range(len(numb)):
        if numb[i] >= minval and numb[i] <= maxval:
            indx.append(i)
    return indx


n = int(input('Введите количество элементов в массиве: '))
array1 = arr(n)
print(f'Системой определен вот такой массив: {array1}')

min_val = int(input('Введите нижнее значение диапазона: '))
max_val = int(input('Введите верхнее значение диапазона: '))



result = find_indx(array1, min_val, max_val)
print(*result)