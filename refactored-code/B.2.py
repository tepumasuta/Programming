num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

while num2:
	num1, num2 = num2, num1 % num2

print()
print(f'Наибольший общий делитель: {num1}')
