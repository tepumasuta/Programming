sum = 0
div = 1
sign = 1
while 1 / div ** 2 > 0.01 / 2:
      sum += (1 / div ** 2) * sign
      div += 1
      sign = -sign
print(abs((sum * 12) ** (1 / 2)))
      
