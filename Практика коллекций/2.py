# Найти все числа, кратные 9, больше 80 и меньше 900, признак окончания ввода  --  пустая строка

# Как делали раньше
#
# n = input()
# k = 0
#
# while n != '':
#     if n.isdigit():
#         if int(n) % 9 == 0 and 80 < int(n) < 900:
#             k += 1
#
#     n = input()
#
# print(k)

# Как можно сейчас
# Найти все различные элементы во входящем потоке

ins = []
n = input()
k = 0


while n != '':
    ins.append(n)
    n = input()

for i in ins:
    if i.isdigit():
        if int(i) % 9 == 0 and 80 < int(i) < 900:
            k += 1

diff_elements = set(ins)

print(diff_elements, k)




