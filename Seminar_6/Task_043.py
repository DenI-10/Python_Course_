# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.

# Ввод:         Вывод:
# 1 2 3 2 3     2

list = [int(i) for i in input().split()]
print(list)

def pars(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                count += 1
    print(count)

pars(list)