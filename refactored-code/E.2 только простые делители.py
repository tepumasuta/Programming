import sys

true_number = int(input('Введите число: '))

if true_number < 1: 
	print('Не, не, так дело не пойдёт')
	sys.exit(0)

number = true_number
print('Простые делители: ', end='')

while number != 1:
	for divisor in range(2, number + 1):
			if number % divisor == 0:
				print(divisor, end=' ')
				number //= divisor
				break



print()

number = true_number
print('Простые делители: ', end='')

for divisor in range(2, number):
	while number % divisor == 0:
		print(divisor, end=' ')
		number //= divisor

	if number == 1: break