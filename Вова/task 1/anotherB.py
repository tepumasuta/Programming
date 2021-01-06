a = int(input())
S = 0

while a != 0:
	length = len(str(a))
	S += a // 10 ** (length - 1)
	a %= 10 ** (length - 1)

print(S)

# Если мы на тот момент не проходили функцию len:

def my_len(x):
	out = 0
	while x != 0:
		x //= 10
		out += 1
	return out

a = int(input())
S = 0

while a != 0:
	length = my_len(a)
	S += a // 10 ** (length - 1)
	a %= 10 ** (length - 1)

print(S)

# Если мы не проходили функции

a = int(input())
S = 0

while a != 0:
	length = 0
	x = a
	while x != 0:
		x //= 10
		length += 1
	S += a // 10 ** (length - 1)
	a %= 10 ** (length - 1)

print(S)