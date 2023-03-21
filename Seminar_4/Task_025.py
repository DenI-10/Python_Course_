# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 * используйте функцию .split()

my_str = input()
dict = {}
my_list = my_str.split()
print(my_list)
for i in my_list:
    if i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}',end = ' ')
    else: 
        dict[i] = 0
        print(i,end=" ")
print()

# Этот вариант, если нужно split применить обязательно
print('Этот вариант, если нужно split применить обязательно')
my_list = my_str.split()
print(my_list)
for i in range(len(my_list)):
  if my_list.count(my_list[(i + 1) * -1]) > 1:
    my_list[(i + 1) * -1] += f'_{str(my_list.count(my_list[(i + 1) * -1]) - 1)}'
print(my_list)

# Этот вариант больше похож на пример в задании
print('Этот вариант больше похож на пример в задании')
print(my_str)
new_str = ''
for i in range(len(my_str)):
  if my_str[i] != ' ' and my_str.count(my_str[i], 0, i) > 0:
    new_str += f'{my_str[i]}_{my_str.count(my_str[i], 0, i)}'
  else: 
    new_str += my_str[i]
print(new_str) 
