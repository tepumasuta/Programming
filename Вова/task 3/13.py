# Дано
# Мне не дано

# 1
print('Вариант 1')
lst = []
for _ in range(3):
	first = []
	for _ in range(4):
		second = []
		for _ in range(6):
			second.append('*')
		first.append(second.copy())
	lst.append(first.copy())
print(lst, end='\n\n')

# 2
print('Вариант 2')
lst = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(lst, end='\n\n')

# 3
print('Вариант 3')
def gen_3d_list(x, y, z):
	def iter_(now_lst, depth, times, now_depth=0):
		if now_depth == depth:
			now_lst.append('*')
			return
		for _ in range(times[now_depth]):
			a = []
			iter_(a, depth, times, now_depth + 1)
			now_lst.append(a)
		return lst
	
	return iter_([], 3, (x, y, z))

print(gen_3d_list(3, 4, 6))
