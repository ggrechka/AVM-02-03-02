# -*- coding: utf-8 -*-

from math import exp


def f(x):
    return x - exp(-x / 10)

def chord_method(x1, x2, f, eps):
    while abs(x2 - x1) > eps:
        x1, x2 = x2, x1 - ((x2 - x1) * f(x1)) / (f(x2) - f(x1))
    return x2


a = float(input('a = '))
b = float(input('b = '))
eps = float(input('eps = '))
print('x =', chord_method(a, b, f, eps))

# входные данные
# a = 0
# b = 1
# eps = 0.001

# выходные данные
# x = 0.9127651474614689
