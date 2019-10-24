import math


def func(x):
    return (x+5) ** 4


def compare(a, x1, x2, b):
    if abs(func(x1) - func(2)) < 0.000001:
        return x1, x2
    elif func(x1) > func(x2):
        return a, x1
    else:
        return x2, b


def dih(a, b, eps):
    sig = eps/4
    while abs(a - b) > eps:
        x1 = (a + b)/2 - sig
        x2 = x1 + 2 * sig
        a, b = compare(a,x1, x2,b)
    return a


def sech(a, b, eps):
    while abs(a - b) > eps:
        x1 = a + (3 - math.sqrt(5)) / 2 * (b-a)
        x2 = a + (math.sqrt(5) - 1) / 2 * (b-a)
        a,b = compare(a,x1,x2,b)
    return a

def F(n):
    if (n <= 2):
        return 1
#    return 1 / math.sqrt(5) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n)
    return F(n-1) + F(n-2)
