# Способ первый
import random
num = random.randint(0, 999999)
print(num)


out_num = 0

while num:
	out_num = num % 10 + out_num * 10
	num //= 10

print(out_num)


# Способ второй
num = int(input('Введите число: '))

out_num = int(str(num)[::-1])
print(out_num)