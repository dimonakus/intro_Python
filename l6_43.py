# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2


import random

def arr(a):
    list1 = []
    for i in range(a):
        list1.append(random.randint(1, 20))
    return list1

def compare_arr(list_):
    count = 0
    for item in set(list_):
        # if list_[i] == list_[i+1]:
        #     count +=1
        count += list_.count(list_[item]) // 2
        return count


n = int(input('Введите количество элементов в массиве: '))

array1 = arr(n)
#array1 = [1, 2, 3, 2, 3]
print(array1)
print(compare_arr(array1))

#Решение коллег

list1 = [1, 2, 3, 2, 3]

# def doub_numb(arr):
#     count = 0
#     for item in set(arr):
#         count += arr.count(item) // 2
#     return count

# print(doub_numb(list1))

