# Дано
import random
print('Инициализируем условие')
lst = [random.randrange(-99999, 99999) for _ in range(1, 99999)]  # Список даётся
print(end="\n\n")


# 1
print('Вариант 1')
product = 1

for i in lst:
	product *= i

print(product, end="\n\n")

# 2
print('Вариант 2')
import operator
import functools

print(functools.reduce(operator.mul, lst, 1), end="\n\n")

# 3
print('Вариант 3')
import functools

print(functools.reduce(lambda x, y: x * y, lst, 1))
