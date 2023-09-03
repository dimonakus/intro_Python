# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simple(n):
    # if n % 1 == 0 and n % n == 0:
    #     return print('yes')
    #count = 0
    for i in range(2, n//2):
    
        if n % i == 0:
            #count += 1
            return 'no'
    return 'yes'    

number = int(input('Введите число: '))
print(simple(number))