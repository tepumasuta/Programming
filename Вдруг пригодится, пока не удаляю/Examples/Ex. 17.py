x = 10
y = 0

try:
	print(x / y)
	print("Сейчас я не выполнюсь")
except ZeroDivisionError:
	print("Делить на ноль нельзя")
print()


x = 10
y = 1
try:
	print(x / y)
	print(x / 0)
except ZeroDivisionError as e:
	print("Делить на ноль нельзя")
else:
	print("Всё прошло успешно")
print()


x = 10
y = 1
try:
	print(x / y)
except ZeroDivisionError as e:
	print("Делить на ноль нельзя")
else:
	print("Всё прошло успешно")
print()


try:
	a = int(input("Введите целое число: "))
	b = int(input("Введите целое число: "))
except ValueError:
	print("Сказали же, целое число")
else:
	print(f'Их сумма: {a + b}')
finally:
	print("Я выполняюсь всегда", end="\n\n")

try:
	print(10 + '10')
except TypeError:
	print("Складывать разные типы нельзя")
finally:
	print()


b = input()
try:
	a = int(input())
	print(a + b)
except ValueError as e:
	print(e.args)
except TypeError:
	print("Нельзя складывать разные типы")
else:
	print("Ну, всё ок")
finally:
	print()


b = input()
try:
	a = int(input())
	print(a + b)
except (ValueError, TypeError):
	print("Ошибка")
finally:
	print()