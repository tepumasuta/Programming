a = (input("Введите число: "))


try:
 a = int(a)
 print(a)
except ValueError:
	a = int()

print(a // 10)


