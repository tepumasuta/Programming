# Дано
print("Инициализируем условие")
import random
letters = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
	       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
	       'x', 'y', 'z', '\\', '|', '/', '_', '+', '-', '=') + ('',) * 1000
n = random.randint(0, 50)
string = ' '.join([''.join([random.choice(letters) for _ in range(random.randint(0, 1000))]) for _ in range(random.randint(0, 100))])
print(end='\n\n')

# 1
print('Вариант 1')
words = []
for word in string.split(' '):
	if len(word) > n:
		words.append(word)
print(words, end='\n\n')

# 2
print('Вариант 2')
import functools
words = list(filter(lambda x: functools.reduce(lambda z, y: z + 1, x, 0) > n, string.split(' ')))
print(words, end='\n\n')

