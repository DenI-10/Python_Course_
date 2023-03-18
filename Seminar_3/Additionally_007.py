# Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random
n = int(input("Введите число элементов:"))
list_1 = [random.randint(-50,50) for item in range(n)]
print(list_1)
local_max = list_1[0]
for i in range(1, len(list_1)-1):
    if list_1[i-1] < list_1[i] > list_1[i + 1]:
        local_max = i
print(local_max) 