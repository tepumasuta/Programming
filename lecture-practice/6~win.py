num = int(input())
out_num = 0
while num != 0:
	num1 = num % 10
	num //= 10
	out_num = num1 + out_num * 10

print(out_num)
