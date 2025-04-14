import math

a, b = float(input()), float(input())

numbers = [a, b]
prod = math.prod(numbers)

ari = sum(numbers) / 2
geo = math.pow(prod, 1 / len(numbers))
harm = len(numbers) / sum(1 / x for x in numbers)
quadr = math.sqrt(sum(x ** 2 for x in numbers) / len(numbers))

print(ari, geo, harm, quadr, sep='\n')
