num1 = int(input())
num2 = int(input()) 
while num2 != 0:
      mod1 = num1 % num2
      num1 = num2
      num2 = mod1
print(num1)
