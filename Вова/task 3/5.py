# Дано
print('Инициализируем условие')
import random
import string
letters = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
	       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
	       'x', 'y', 'z', '\\', '|', '/', '_', '+', '-', '=') + ('',) * 1000
lst = [''.join([random.choice(letters) for _ in range(45)]) for _ in range(9999)] + ['']
print(end='\n\n')

# 1
print('Вариант 1')
amount = 0

for word in lst:
	if len(word) > 1 and word[0] == word[-1]:
		amount += 1

print(amount, end='\n\n')

# 2
print('Вариант 2')
import functools
cond1 = lambda x: x[0] == x[-1] if x != '' else True
cond2 = lambda x: functools.reduce(lambda z, y: z + 1, x, 0) > 1

print(functools.reduce(lambda x, y: x + y, map(lambda f: cond1(f) and cond2(f), lst)))

