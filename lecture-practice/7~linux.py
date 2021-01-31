import random
num = random.randrange(100)

while True:
	if num == 13:
		print('О господи, выхожу из цикла!!!')
		break
	elif num <= 0:
		print('Закончили.')
	else:
		print(num)
		num -= 1


def iterate(num):
	if num == 13:
		print('О господи, выхожу из цикла!!!')
		return None
	elif num <= 0:
		print("Закончили.")
		return None
	else:
		print(num)
		return iterate(num - 1)

iterate(random.randrange(100))








# function = lambda: None

# # чистые/нечистые

# print  # нечистая
# sum  # чистая

# function()
# function()

# new_function = function

# new_function()
# function()

# print(new_function())
# a = function()