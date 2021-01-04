# Как можно создать список из входных данных
# Если у нас есть конкретное число элементов

a = []
for i in range(300):
    a.append(input())

a = [0] * 300
for i in range(300):
    a[i] = input()

a = [input() for i in range(300)]

# Если у нас неопределённое кол-во элементов
b = input()

while b != '':
    a.append(b)
    b = input()
