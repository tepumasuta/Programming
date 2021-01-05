# Дано
print('Инициализируем условие')
import random
lst = [i for i in range(1, random.randint(2, 10))]
print(f'lst: {lst}', end='\n\n')

# 1
print('Вариант 1')
import itertools
perms = list(itertools.permutations(lst))
print(perms, end='\n\n')

# 2
print('Вариант 2')
def permutations(lst):
	def repeated_for(lst, now=tuple(), out=[]):
		def removed_list(lst, item):
			new_lst = lst.copy()
			new_lst.remove(item)
			return new_lst

		if not lst:
			out.append(now)
		else:
			for i in lst:
				repeated_for(removed_list(lst, i), now + (i,), out)
		return out

	return repeated_for(lst)

perms = permutations(lst)
print(perms, end='\n\n')

# 3
# print('Вариант 3')
# def removed_list(lst, item):
# 	new_lst = lst.copy()
# 	new_lst.remove(item)
# 	return new_lst

# repeated_map = lambda lst, now=tuple(): list(map(lambda x: repeated_map(removed_list(lst), now + (x,)), lst)) if not lst else now


# perms = repeated_map(lst)
# print(perms)
