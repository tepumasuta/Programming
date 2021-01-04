# immutable
# целые числа (int), числа с плавающей точкой (float), комплексные числа (complex), 
# логические переменные (bool), кортежи (tuple), строки (str) и неизменяемые множества (frozen set)
x = int(7)
y = float(0.9)
z = complex(80, 64)
flag = bool(7 > 0)
T = tuple([1, "hi", 99.994])
string = str('abc')
consts = frozenset(set(5, 4, 34, 6, 35))

# mutable
# списки (list), множества (set), словари (dict)
A = [1, 2, 3]
elements = set(9, 3, 23)
first_lastnames = dict(('Vasya', "Pupkin"), ('Jenny', 'Smith'),
	                   ("Alla", 'Allanovskaya'), ("El", "K"))
