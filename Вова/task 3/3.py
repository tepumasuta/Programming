# Дано
import random
print('Инициализируем условие')
lst = [random.randrange(-9999999999, 9999999999) for _ in range(9999999)]  # Список даётся
print(end="\n\n")


# 1
print('Вариант 1')
maximum = -float('inf')
for i in lst:
	if i > maximum:
		maximum = i

print(maximum, end="\n\n")

# 2
print('Вариант 2')

copy_lst = lst.copy()
copy_lst.sort()

print(copy_lst[-1], end='\n\n')

# 3
print('Вариант 3')
import functools

print(functools.reduce(lambda x, y: (x, y)[y > x], copy_lst, -float('inf')))
