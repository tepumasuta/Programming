summ = 0
sign = 1
divisor = 1

while 1/divisor > 0.01 / 2:
	summ += (1 / divisor) * sign
	sign = -sign
	divisor += 2

print(summ * 4)
