import random
l = [random.randint(-999999, 999999) for _ in range(2)]
print(f'Исходный список: {l}', end='\n\n')

max1 = -float("inf")

for num in l:
	if num > 3 and num % 8 == 0 and num > max1:
		max1 = num
print(max1, max(l))
