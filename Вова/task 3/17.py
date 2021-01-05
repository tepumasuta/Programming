# 1
print('Вариант 1')
lst = [i ** 2 for i in range(5, 30)]
print(lst, end='\n\n')

# 2
print('Вариант 2')
lst = list(map(lambda x: x ** 2, range(5, 30)))
print(lst)
