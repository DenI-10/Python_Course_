# Шахматный конь ходит буквой "Г" - на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. 
# Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом. 
# В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())   

if (x1 - x2) * (y1 - y2) == 2 or (x1 - x2) * (y1 - y2) == -2:
     print('yes')
else:
    print('no')
    