# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

import math

N = int(input("Введите число N: "))

factorial = []

for i in range(1, N+1):
    factorial.append(math.factorial(i))

print(N, "! =", factorial)