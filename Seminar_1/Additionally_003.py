# Пользователь вводит целое число. 
# Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "
# положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число".

a = int(input())
if a > 0:
    if a % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
elif a < 0:
    if a % 2 == 0:
        print("отрицательное четное число")
    else:
        print("отрицательное нечетное число")
else:
    print("Нулевое число")