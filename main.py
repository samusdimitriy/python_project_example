import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

P = a + b + c
p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("P = ", P)