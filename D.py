from math import sqrt
a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4 * a * c
x1 = (-b + sqrt(D)) / 2*a
x2 = (-b - sqrt(D)) / 2*a
print(x1, x2)