T = 1, 2, 3, 2


# T.count(value)  --  Считает, сколько value в кортеже. Принимает ровно 1 аргумент

print(T.count(1))
print(T.count(2))
print()

print(T.count(0))
print()

# print(T.count())  --  Ошибка
# print()

# print(T.count(1, 2))  --  Ошибка
# print()


# T.index(value, [start, [stop]]) Возвращает индекс value. Принимает 1, 2 или 3 аргумента
# Первый - значение, второй - откуда считать (по умолчанию = 0),
# третий - до куда считать, не включая (по умолчанию = длине кортежа)
# Квадратные скобки  --  необязательный аргумент
# Если значение не найдено - вызывает ошибку

print(T.index(1))
print(T.index(2, 1))
print(T.index(2, 2, 4))
# print(T.index(2, 2, 2))  --  Ошибка
print()
