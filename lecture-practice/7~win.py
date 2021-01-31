import random

def my_input():
	return random.randint(0, 100)

my_list = list()

for _ in range(20):
	my_list.append(my_input())
print(my_list)
