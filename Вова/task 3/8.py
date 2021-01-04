# Дано
print('Инициализируем условие')
import random
lst = [random.randint(0, 10) for _ in range(random.randint(1, 10))] if random.randint(0, 1) else []
print(end='\n\n')

# 1
print('Вариант 1')
if lst == []:
	print(True)
else:
	print(False)
print()

# 2
print('Вариант 2')
if not lst:
	print(True)
else:
	print(False)
print()

# 3
print((True, False)[bool(lst)])
