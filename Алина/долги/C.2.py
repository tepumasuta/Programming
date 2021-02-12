num = int(input())
am = 0
for i in range(1, num + 1):
      if num % i == 0:
            am += 1
if am == 2:
      print("простое")
else:
      print("составное")
