import random

input = []
randnum = 0
minus = 0
plus = 0

while randnum < 15:
    randnum = randnum + 1
    input.append(random.randint(0, 100))
    input.append(random.randint(-100, 0))

for check in input:
    check = int(check)
    if check < 0:
        minus = minus + check
    else:
        plus = plus + check
print("Список чисел: ", input)

print(minus, plus)