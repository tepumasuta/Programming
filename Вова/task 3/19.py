# Дано
print('Инициализируем условие')
import random
lst1 = [random.randint(0, 10000) for _ in range(random.randint(0, 1000))]
lst2 = [random.randint(0, 10000) for _ in range(random.randint(0, 1000))]
print(end='\n\n')

# 1
print('Вариант 1')
inter = list((set(lst1) - set(lst2)) | (set(lst2) - set(lst1)))
print(inter, '\n', len(inter), end='\n\n')

# 2
print('Вариант 2')
inter = []
for i in lst1:
	if i not in lst2:
		inter.append(i)
for i in lst2:
	if i not in lst1:
		inter.append(i)
print(inter, len(inter), end='\n\n')
