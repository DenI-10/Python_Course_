#За день машина проезжает n километров. 
#Сколько дней нужно, чтобы проехать маршрут длиной m километров?
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input())
m = int(input())
print((n+m -1)//n)
