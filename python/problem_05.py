import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


num = 1
for i in range(1, 21):
    num = lcm(num, i)

print("Solution is: " + str(num))
