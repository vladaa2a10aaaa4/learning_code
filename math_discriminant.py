import math

a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * (a * c)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    root1, root2 = sorted([x1, x2])
    print(root1, root2, sep='\n')
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')
