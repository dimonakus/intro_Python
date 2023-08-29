# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = input('Введите строку: ').split()
print(text)

dct = {}
for char in text:
    if char in dct.keys():
        print(f'{char}_{dct[char]}', end = ' ')
        #dct[char] += 1

    else:
       # dct[char] = 1
        print(char, end =' ')

    dct[char] = dct.get(char, 0) + 1
        