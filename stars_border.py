n = int(input())
width = 19  # Ширина рамки (можно сделать динамической)

border = '*' * width
middle = '*' + ' ' * (width - 2) + '*'

print(border)
for _ in range(n - 2):
    print(middle)
if n > 1:  # Чтобы избежать дублирования при n=1
    print(border)
