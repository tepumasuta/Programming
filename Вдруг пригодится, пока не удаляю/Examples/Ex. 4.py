a = '123'
b = int(a)
c = int(str(int('abc', 23)), 8)
print(a, b, c)

print(b.as_integer_ratio(), c.bit_length(), int(a).conjugate())
print(int('aaaa', 11), int(), int(int(8)), end="\n\n")



a = float('0.123')
b = float()
c = float(float(7.0))
d = int(float(9.7))

print(a, b, c)
print(float(9.7), d)

print(a.as_integer_ratio(), b.conjugate(), c.is_integer(), float(9.7).is_integer())
print()
print(a.hex(), type(a.hex()), float(9.7).hex(), float.fromhex(float(9.7).hex()),
      a.fromhex(c.hex()), a, end="\n\n")



a = complex()
b = complex(2)
c = complex(3, 4)
d = 5 + 8 * 1j
q = 7 + 0 * 1j

print(a, b, c, d, q)
print(type(c), type(d), type(q))