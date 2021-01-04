# print(value, ..., sep=' ', end='\n', file=sys.stdout)
# принимает значение или значения и выводит их в file или поток. По умолчанию выводит в консоль
# sep - разделитель, ставящийся между всеми значениями
# end - то, что ставиться после всех значений, по умолчанию "\n"


print(1)
print(1, 2, 3, 4)
print()
print(1, 2, 3, 4, sep="")
print(1, 2, 3, 4, end="мда\n")
print(1, 2, 3, 4, sep="_", end="конец")
print(1, end="\n\n")


# id()  --  возвращает идентификатор, с которым связано имя или переданный объект
a = 5
print(id(a), id(1), sep="\n")

a = 4
print(id(a), id(1), sep="\n", end="\n\n")  # Что удивительно, сборщик мусора не сожрал 1


# type(object) - возвращает тип объекта
a = 5
b = 0.5
c = 4 + 5j
T = 1, 2, 3
A = [4, 2, 2, 4, 42]

print(type(a), type(b), type(c), type(T), type(A), type(type(a)), sep="\n", end="\n\n")


# sorted(iterable object, key=None, reverse=False) Возвращает новый отсортированный iterable object
# Сортирует по возрастанию
# key  --  функция от одного аргумента, применящаяся к каждому элементу iterable object перед сравнением
# reverse  --  если true, вернёт отсортированный iterable object задом наперёд
def user_key(x):
    return x ** 2


A = [-1, 1, 2, 3, 0.88, 0.89, -1]
B = 1, 5, 6, 4, 9

print(sorted(A, key=user_key), sorted(B), sep="\n", end="\n\n")


# ord(value) value - строка из одного символа. Возвращает численное значение символа
print(ord("3"), ord("A"), ord("a"), ord("Ф"), ord("А"), sep="   ", end="\n\n")


# chr(i)  --  преобразует число в строку состаящую из одного символа, соответсвующего данному индексу
print(chr(76), chr(1040), sep="\n", end="\n\n")


# len(sequnce/mapping object) возвращает кол-во элементов в последовательности (sequence) или mapping object
# и нет только в целом object: Объект-контайнер, число элементов в котором требуется определить.
a = 1, 2, 3
b = 'ssdgsdffdsf'
print(len(a), len(b), sep="\n", end="\n\n")


#  operator.itemgetter(i) Вообще это не совсем функция. Она создаёт вызываемый объект. Но не суть, о чём эта
#  функция: Она принимает аргумент или список таковых. И возвращает вызывамый объект. То есть:
#  После f = itemgetter(2), мы можем вызвать f(r) и оно вернёт r[2]
#  После g = itemgetter(2, 5, 3) и вызыва g(r) вернётся следующий кортеж (r[2], r[5], r[3])
#  Ну и раз эта функция возвращает объект, то его можно и не запоминать никуда. То есть мы моем сделать так:
#  itemgetter(1)(r) и вернёт оно соответственно r[1]
import operator
a = operator.itemgetter(1)
T = 1, 2, 3
A = ['sad', (2, 4, 32.2), 0]
print(a(T), a(A), operator.itemgetter(1)(A), operator.itemgetter(1)(T), sep="\n", end="\n\n")

#  range([start ,] stop[, step])  --  генератор арифметических прогрессий. Возвращает прогрессию, сгенерированную
#  начиная с start, с шагом step, пока член прогрессии < stop
#  По умолчанию start = 0, step = 1
#  Итерируемый объект
a = range(10)
print(len(a))
for i in a:
	print(i)
a = range(0, 98, 5)
for i in a:
	print(i - 1)
for i in range(500, 87, -1):
	print(i)
del(a)

#  del(obj)  Deletion of a target list recursively deletes each target, from left
# to right.

# Deletion of a name removes the binding of that name from the local or
# global namespace, depending on whether the name occurs in a "global"
# statement in the same code block.  If the name is unbound, a
# "NameError" exception will be raised.

# Deletion of attribute references, subscriptions and slicings is passed
# to the primary object involved; deletion of a slicing is in general
# equivalent to assignment of an empty slice of the right type (but even
# this is determined by the sliced object).

# Changed in version 3.2: Previously it was illegal to delete a name
# from the local namespace if it occurs as a free variable in a nested
# block.

# Related help topics: BASICMETHODS
a = 7
del(a)  # стирает a


