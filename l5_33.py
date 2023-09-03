# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1




def maximum(est2):
    maximum = max(est2)
    minimum = min(est2)
    for i in range(len(est2)):
        if est2[i] == minimum:
           est2[i] = maximum


est = list(input('Введите оценки: '))

print(maximum(est))

#Решение коллег

# import random


# def number(list2):
#     maximum = max(list2)
#     minimum = min(list2)
#     for i in range(len(list2)):
#         if list2[i] == maximum:
#             list2[i] = minimum

# list1 = [random.randint(1,5) for i in range(5)]
# print(list1)
# number(list1)
# print(list1)