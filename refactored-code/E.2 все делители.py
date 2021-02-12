num = int(input('Введите целое число: '))

print('Простые делители: ')

for divisor in range(1, num + 1):
	if not num % divisor: print(divisor, end=' ')
