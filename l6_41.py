# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

import random

def arr(a):
    list1 = []
    for i in range(a):
        list1.append(random.randint(1, 20))
    return list1

def comp(list_):
    count = 0
    for i in range(1, len(list_)-1,):
        if list_[i] > list_[i+1] and list_[i] > list_[i-1]:
            count +=1
    return count

n = int(input('Введите количество элементов в массиве: '))

array1 = arr(n)
print(array1)
print(comp(array1))
