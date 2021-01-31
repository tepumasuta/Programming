# Дано
print('Инициализируем условие')
import random
lst = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 100))]
print(end='\n\n')

# 1
print('Вариант 1')
string = ''.join(lst)
print(string, end='\n\n')

# 2
print('Вариант 2')
string = ''
for char in lst:
	string += char
print(string, end='\n\n')

# 3
print('Вариант 3')
import functools
string = functools.reduce(lambda x, y: x + y, lst)
print(string)
