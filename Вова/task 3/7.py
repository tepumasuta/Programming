# Дано
print('Инициализируем условие')
import random
letters = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
	       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
	       'x', 'y', 'z', '\\', '|', '/', '_', '+', '-', '=') + ('',) * 1000
lst = [''.join([random.choice(letters) for _ in range(random.randint(0, 1000))])] + \
       [random.randint(random.randint(0, 1000), random.randint(1000, 1000000)) for _ in range(9999)] + \
       [tuple([random.randint(0, 100) for _ in range(random.randint(2, 10))]) for _ in range(random.randint(0, 100))]
random.shuffle(lst)
print(end='\n\n')

# 1
print('Вариант 1')
print(list(set(lst)), end='\n\n')

# 2
print('Вариант 2')
tmp_lst = []
for item in lst:
	if item not in tmp_lst:
		tmp_lst.append(item)
print(tmp_lst)
