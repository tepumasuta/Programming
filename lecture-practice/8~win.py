import random
l = [random.randint(0, 100) for _ in range(5)]
print(f'Исходный список: {l}', end='\n\n')


print(sum(l))