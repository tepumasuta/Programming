A = [1, 2, 3]

print(A, end="\n\n")


# A.append(object) добавляет object в конец списка

A.append(4)
print(A, end="\n\n")


# A.extend(iterable object) добавляет все объекты из iterable object в конец списка A

B = [2, 4, 6]
A.extend(B)

print(A, B, end="\n\n", sep="\n")


# A.count(), A.index() аналогично с кортежами tuple

print(A.count(2), A.index(4, 2, 6), sep="\n", end="\n\n")


# A.insert(index, object) вставляет элемент на индекс index, все остальные при этом сдвигаются вправо на 1
# Если insert > длины кортежа, то вставляет в конец, если меньше 0, вставляет в начало

A = [1, 2, 3]

A.insert(-1, 7)
A.insert(99999, 6)
A.insert(3, 91)
print(A, end="\n\n")
