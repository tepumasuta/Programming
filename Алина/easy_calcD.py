s = 0
x = 1
z = 1
for i in range(10):
	s += (4 / x) * z
	x += 2
	z = -z
print(s)