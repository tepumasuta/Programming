# Дано
import random
lst = [random.randint(0, 10) for _ in range(random.randint(0, 10))]
print(end='\n\n')

# 1
print('Вариант 1')
for index, value in enumerate(lst):
	print((index, value))
print()

# 2
print('Вариант 2')
for i in range(len(lst)):
	print((i, lst[i]))
print()

# 3
print('Вариант 3')
import functools
import collections
collections.deque(map(lambda x: print((x[0], x[1])), enumerate(lst)))
