# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

#Пишем через функции
import random

def arr(a):
    list1 = []
    for i in range(a):
        list1.append(random.randint(1, 20))
    return list1

def dif_arr (ar1, ar2):
    for i in range(len(ar1)-1,-1,-1):
        #for j in range(len(ar2)):
        #    if ar2[j] == ar1[i]:
            if ar1[i] in ar2:
                print(ar1.pop(i))
    return ar1
                
n, m = map(int, input('Введите количество элементов массива: ').split())

array1 = arr(n)
print(array1)

array2 = arr(m)
print(array2)

print(dif_arr(array1, array2))
