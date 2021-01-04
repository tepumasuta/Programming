# Дано
print("Инициализируем условие")
import random
lst = [random.randint(0, 10) for _ in range(random.randint(0, 10))]
print(end='\n\n')

# 1
print("Вариант 1")
copy_lst = lst.copy()
print(copy_lst, end='\n\n')

# 2
print("Вариант 2")
copy_lst = lst[:]
print(copy_lst, end='\n\n')

# 3
print("Вариант 3")
import copy
copy_lst = copy.copy(lst)
print(copy_lst, end='\n\n')

# 4
print("Вариант 4")
import copy
copy_lst = copy.deepcopy(lst)
print(copy_lst, end='\n\n')

# 5
print("Вариант 5")
copy_lst = list(lst)
print(copy_lst)
