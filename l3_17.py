#Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

numbers = list(map(int, input('Введите произвольные числа через пробел: ').split()))
print(len(set(numbers)))