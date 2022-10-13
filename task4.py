# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.

import math

number = float(input("Введите число N: "))
number = abs(number)
x = math.floor(number)

list = []

for i in range(-x, x+1):
    list.append(i)

print()
print("Получившийся список: ", list)

list = list[-2:] + list[:-2]
print()
print("Список со слвигом элементов на 2 вправо: ", list)
print()