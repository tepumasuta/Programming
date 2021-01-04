# Дано
print('Инициализируем условие')
import random
lst1 = [random.randint(0, 20) for _ in range(random.randint(0, 10))]
lst2 = [random.randint(0, 20) for _ in range(random.randint(0, 10))]
print(end='\n\n')

# 1
print('Вариант 1')
def intersection1(list1, list2):
	for i in list1:
		for j in list2:
			if i == j:
				return True
print(intersection1(lst1, lst2), end='\n\n')

# 2
print('Вариант 2')
intersection2 = lambda list1, list2: (None, True)[bool(set(list1) & set(list2))]
print(intersection2(lst1, lst2), end='\n\n')
