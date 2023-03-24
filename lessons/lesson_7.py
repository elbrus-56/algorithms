# Алгоритм Евклида
"""
Эффективный алгоритм для нахождения наибольшего общего делителя двух
целых чисел (или общей меры двух отрезков).
"""


def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


print(gcd(12, 4))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 4))
