# Дано
print('Инициализируем условие')
import random
lst = [i for i in range(random.randint(5, 10), random.randint(15, 30))]
print(f'lst: {lst}', end='\n\n')

# 1
print('Вариант 1')
my_lst = lst.copy()
my_lst.pop(0)
my_lst.pop(4)
my_lst.pop(5)
print(my_lst, end='\n\n')

# 2
print('Вариант 2')
my_lst = lst.copy()
for index in 0, 4, 5:
	my_lst.pop(index)
print(my_lst)
