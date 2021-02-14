num = int(input("Введите число: "))
list_of_divs = [1]
am = 0

for div in range(1, num + 1):
      if num % div == 0:
            for i in range(1, div + 1):
                  if div % i == 0:
                        am += 1
      if am == 2:
             list_of_divs.append(div)
      am = 0
print(list_of_divs)
                        
