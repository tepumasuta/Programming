# Если нас интересует с переводом строки

for i in range(179):
	print('Python')

# или

print('Python\n' * 179)


# Если нас интересует без пробелов

for i in range(179):
	print('Python', end='')


# или

print('Python' * 179)