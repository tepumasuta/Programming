string = "ABC"
string.capitalize()  # Возвращает копию строки с первой буквой заглавной, а остальными нет

string1 = "abc"
string2 = "aBc"

print(string.capitalize(), string1.capitalize(), string2.capitalize(), end="\n\n", sep="\n")


# center(width, [fillchar])  --  возвращает строку, отцентрованную в другой строке длиной width из fillchar
# По умолчанию fillchar = " ". Длина fillchar  --  1
string = "abcdef"
print(string.center(20), string.center(9, "_"), sep="\n", end="\n\n")


# string.count(sub, [start, [end]]) Считает сколько в строке string подстрок sub начиная с start и заканчивая end - 1
# По умолчанию start = 0, end = len(string)
string = "apple"
print(string.count("p"), string.count("a", 2), string.count("pl", 1, 4), sep="\n")

string1 = "alala"
string2 = "alaala"
print(string1.count("ala"), string2.count("ala"), sep="\n", end="\n\n")

# string.encode([encoding, [errors]])
# bytes.decode([encoding, [errors]])
# Имя	Что происходит
# strict	Возбуждается UnicodeError (или наследника).
# ignore	Символы пропускаются.
# replace	Символы заменяются на U+FFFD (REPLACEMENT CHARACTER).
# (3.5)backslashreplace	Символы заменяются на последовательности, начинающиеся с обратной косой черты (слеша).
# (3.1)surrogateescape	Заменяет каждый байт на код суррогата (от U+DC80 до U+DCFF).
# (3.1)surrogatepass	Игнорирует в строке коды суррогатов. Используется со следующими кодеками:
#  utf-8, а также начиная с 3.4 utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le.
string = "apple"
print(string.encode())
print(string.encode().decode())

string1 = 'котобус cat'.encode()

print(type(string1), string1.decode(), string1.decode('ascii', errors='backslashreplace'),
'котобус cat'.encode().decode('ascii', errors='surrogateescape'), sep="\n", end="\n\n")


# string.endswith(suffix, [start, [end]])  --  проверяет, оканчивается ли строка suffix
# start - откуда, end - до куда
string = "abc"
print(string.endswith('c'), string.endswith('bc'), string.endswith('q'), string.endswith('a', 0, 1),
	sep="\n", end="\n\n")


# string.expandtabs([tabsize]) заменяет табы пробелами. по умолчанию таб - 8 пробелов
string = 'a\tb\t\tc'
print(string.expandtabs())
print(string.expandtabs().replace(' ', "п"), string.expandtabs().replace('\t', "т"))
print(string)
print(string.replace(' ', "п"), string.replace('\t', "т"))
print(string.expandtabs(4))
print(string.expandtabs(4).replace(' ', "п"), string.expandtabs(4).replace('\t', "т"))
print('\t'.expandtabs().count(" "), end="\n\n")


# string.find(sub, [start, [end]])  --  находит подстроку в указанном промежутке в строке и возвращает
# индекс начала строки
# По умолчанию start = 0, end = len(string)
# Если не находит возвращает -1
string = "abc"
print(string.find("b"), string.find("z"), string.find("ab"), string.find('bc'), 
	  "abcdef".find("b", 3), "abcdefghijklmnopqrstuvwxyz".find("h", 5, 24), end="\n\n")

# string.index(sub, [start, end]) то же, что и find, но если не находит, вызывает ValueError
string = "abc"
print(string.index("c"))

# string.isalnum() возвращает правду, если string состоит только из чисел и букв
# То есть возвращает правду, если string это alphanumeric(не знаю, как будет на русском) строка 
print(''.isalnum(), 'a'.isalnum(), '1'.isalnum(), '1ds'.isalnum(), '\n'.isalnum(), 'a\n'.isalnum(),
	  "A".isalnum(), "б".isalnum(), end="\n\n")

# string.isalpha() возвращает правду, если string состоит только из букв
# То есть возвращает правду, если string это alphabetic строка
print(''.isalpha(), "a".isalpha(), "1".isalpha(), '\n'.isalpha(), 'A'.isalpha(), 'a\n'.isalpha(),
	  end="\n\n")

# string.isdigit() как isalpha, но для чисел
