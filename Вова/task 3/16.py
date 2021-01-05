# 1
print('Вариант 1')
import random
start = random.randint(0, 20)
end = random.randint(start + 10, 30)
lst = []
for number in range(start, end):
	lst.append(number ** 2)
first_five = lst[0:5]
last_five = lst[-1:-6:-1]
print(first_five, last_five, end='\n\n')

# 2
print('Вариант 2')
import random
start = random.randint(0, 20)
lst = [i ** 2 for i in range(start, random.randint(start + 10, 30))]
first_five = lst[0:5]
last_five = lst[-1:-6:-1]
print(first_five, last_five, end='\n\n')
