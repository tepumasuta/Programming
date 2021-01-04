# Вводится 20 чисел, найти максимальное, минимальное и сумму всех чисел, кратных 7

# Как решали раньше
# maximum = -float('inf')
# minimal = float('inf')
# S = 0
#
# for i in range(20):
#     n = int(input())
#     if n % 7 == 0:
#         S += n
#
#     if n > maximum:
#         maximum = n
#
#     if n < minimal:
#         minimal = n
#
# print(maximum, minimal, S)

# Как можно ещё

amount = 20
numbers = []


for i in range(amount):
    numbers.append(int(input()))

numbers.sort()
maximum = numbers[-1]
minimal = numbers[0]

S = 0
for i in numbers:
    if i % 7 == 0:
        S += i

print(minimal, maximum, S)
