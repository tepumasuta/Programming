# Дано
import random
print('Инициализируем условие')
lst = [random.randrange(-9999999, 9999999) for _ in range(9999999)]  # Список даётся
print(end="\n\n")


# 1
print('Вариант 1')
summury = 0

for i in lst:
	summury += i

print(summury, end="\n\n")

# 2
print('Вариант 2')
print(sum(lst), end="\n\n")

# 3
print('Вариант 3')
import operator
import functools

print(functools.reduce(operator.add, lst, 0), end="\n\n")

# 4
print('Вариант 4')
import functools

print(functools.reduce(lambda x, y: x + y, lst, 0))
