num = int(input('Введите целое число: '))
prime = True

if num > 1:
	for divisor in range(2, num):
		if num % divisor == 0:
			prime = False
			break
else:
	prime = False

print("Это простое число") if prime else print("Это составное число")