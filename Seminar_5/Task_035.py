# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_simple(n):
    # count = 0
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         count +=1
    # return count == 2 ##вариант2
    # return len([i for i in range(1, n+1) if n % i == 0]) == 2 
    for i in range(2,n):
        if n%i==0:
            return ("No")
    else:
        return ("Yes")
n = int(input())
print(is_simple(n))