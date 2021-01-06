pi_over_four = 0
sign = 1
under = 1

for i in range(10):
	pi_over_four += 1 / under * sign
	sign *= -1
	under += 2

pi = 4 * pi_over_four

print(pi)