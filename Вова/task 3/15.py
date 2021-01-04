# Дано
print('Инициализируем условие')
lst = [i for i in range(-99999, 99999)]
print(end='\n\n')

# 1
print('Вариант 1')
import random
my_lst = lst.copy()
random.shuffle(my_lst)
print(my_lst, end='\n\n')

# 2
print('Вариант 2')
import random
my_lst = lst.copy()
new_lst = []
while my_lst:
	index = random.randint(0, len(my_lst) - 1)
	new_lst.append(my_lst.pop(index))
print(new_lst, end='\n\n')
