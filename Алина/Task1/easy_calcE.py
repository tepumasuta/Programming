a = 1
s = 0
for i in range(364):
	a += a * 0.01
	s = s + a
print(s)