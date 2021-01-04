# Дано
print('Инициализируем условие')
import random
lst = [tuple([random.randint(0, 100) for _ in range(random.randint(2, 10))]) for _ in range(random.randint(0, 100))]
print(end="\n\n")

# 1
print('Вариант 1')
def get_second_item(lst):
	return lst[1]

copy_lst = lst.copy()
copy_lst.sort(key=get_second_item)

print(copy_lst, end='\n\n')

# 2
print('Вариант 2')

print(sorted(lst, key=lambda x: x[1]), end='\n\n')

# 3
print('Вариант 3')
import operator

print(sorted(lst, key=operator.itemgetter(1)))
