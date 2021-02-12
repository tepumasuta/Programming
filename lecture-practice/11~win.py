import math


pi_over_2 = 1
numerator = 2
divisor = 1
step = 0

while abs(math.pi / 2 - pi_over_2) > 0.01 / 2:
	step += 1 

	pi_over_2 *= numerator / divisor

	if step % 2 == 0:
		numerator += 2
	else:
		divisor += 2

print(pi_over_2 * 2)


