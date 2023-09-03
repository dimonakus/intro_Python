# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

#Пример рекурсии на функции факториала, разобранная преподавателем
# def fact(num):
#         #pass #Заглушка
#         if num == 1:
#             return 1
#         print (num)
#         return num * fact(num - 1)
        

# number = 5
# print(fact(number))


def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

number_fib = int(input("Введите число: "))

print(fib(number_fib))