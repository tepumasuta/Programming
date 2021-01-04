T1 = 1, 2, 3
T2 = (1, 2, 3)
# T3 = tuple(iterable object)  --  создаёт кортеж на основе iterable object
# Можно подсунуть и кортеж, будет его копия

print(T1, "\n", T2, "\n", T3)
print()

a, b, c = T1  # Распаковка кортежа. Можно распаковать любой iterable object
print(a, b, c)
print()

a, c, b = T1  # Последовательность важна
print(a, b, c)
print()

a, *args = T1  # "*" обозначает, что args  --  список. То есть первый элемент кортежа
# отправиться в a, а все остальные в args. Также есть **. Это будет обозначать словарь
print(a, args)
print()
print(type(a), type(args))
print()

T1 = (1)
T2 = (1,)  # Чтобы создать кортеж из одного элемента необходимо добавить ",", иначе будет просто объект

print(type(T1), type(T2))
print()

T1 = 1, 2, 3, 4, 5

for i in T1:  # По кортежу и любому iterable object можно пробегаться циклом for
	print(i)
print()
