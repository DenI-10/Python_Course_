# Найти нок и нод

a = int(input('Введите число:'))
b = int(input('Введите число:'))

i = 1
nod = 1

while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        nod = i
    i +=1

lcm = a*b/nod
