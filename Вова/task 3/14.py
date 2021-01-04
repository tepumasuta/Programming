# Дано
print('Инициализируем условие')
import random
lst = [random.randint(0, 10000) for _ in range(random.randint(0, 1000))]
print(end='\n\n')

# 1
print('Вариант 1')
filtered = [i for i in lst if i % 2]
print(filtered, end='\n\n')

# 2
print('Вариант 2')
filtered = []
for i in lst:
	if i % 2 != 0:
		filtered.append(i)
print(filtered, end='\n\n')

# 3
print('Вариант 3')
print(list(filter(lambda x: ~(x % 2), lst)))