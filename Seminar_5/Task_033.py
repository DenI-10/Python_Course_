# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change(arg):
    min = arg[0]
    max = arg[0]
    for i in arg:
        if i < min:
            min = i
        elif i > max:
            max = i
    for i in range(len(arg)):
        if arg[i]==max:
            arg[i] = min
    return arg
n = int(input("Введите количество элементов:"))
arg = [int(input()) for i in range(n)]
print(arg)
print(change(arg))
