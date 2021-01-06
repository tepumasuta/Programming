# Если нас интересует сама величина

start = 1
mul = 1.01

for i in range(364):
	start *= mul

print(start)

# Если нас интересует общий пробег

S = 0
now = 1
mul = 1.01

for i in range(365):
	S += now
	now *= 1.01

print(S)