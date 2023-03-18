# Создайте список из случайных чисел. Найдите второй максимум.

import random
n = int(input("Введите число элементов:"))
list = [random.randint(-50, 50) for item in range(n)]
print(list)
list.sort()
print(list[-2]) 