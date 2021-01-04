a = 4  # Создаётся объект 4 и связывается с именем "a"
b = 5  # Создаётся объект 5 и связывается с именем "b"

print(id(a))
print(id(b))
print()

a = b  # Имя "a" связывается с объектом 5 и объект 4 удаляется сборщиком мусора

print(id(a))
print(id(b))
print()

a = 7  # !!! Т.к. объект типа int - immutable, то создаётся новый объект "7" и связывается с именем a

print(id(a))
print(id(b))
print()

a = [1, 2, 3]
b = a
print(a, id(a))
print(b, id(b))
print()

a[0] = 7
print(a, id(a))
print(b, id(b))
print()

a = 10
b = "hello"
c = (1, 2)

print(type(a), type(b), type(c))
print()
