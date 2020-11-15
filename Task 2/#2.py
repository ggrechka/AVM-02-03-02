#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, pi


def f1(x):
    return 2 * x ** 2


def f2(x):
    return 8 + 2 * x - x ** 2


def f3(x):
    return sin(x) / (cos(x) ** 2 + 1)


def runge_rule(o, s1, s2, eps):
    return o * abs(s2 - s1) < eps


def trapezium_method(a, b, n, f, eps):
    '''
    Метод трапеций.

    Ключевые аргументы:
    [a; b] - отрезок
    n - количество разбиений
    f - функция
    eps - точность
    '''
    h = (b - a) / n
    s = 0
    for i in range(1, n):
        x = a + i * h
        s += f(x)
    return h * ((f(a) + f(b)) / 2 + s)


def parabola_method(a, b, n, f, eps):
    '''
    Метод Симпсона (парабол).

    Ключевые аргументы:
    [a; b] - отрезок
    n - количество разбиений
    f - функция
    eps - точность
    '''
    h = (b - a) / n
    s1 = s2 = 0
    for i in range(1, n, 2):
        x = a + i * h
        s1 += f(x)
    s1 *= 4
    for i in range(2, n, 2):
        x = a + i * h
        s2 += f(x)
    s2 *= 2
    return h / 3 * (f(a) + s1 + s2 + f(b))


a = float(input('a = '))
b = float(input('b = '))
n1 = int(input('n = '))
eps = float(input('eps = '))

n2 = n1
s1 = trapezium_method(a, b, n2, f2, eps)
n2 *= 2
s2 = trapezium_method(a, b, n2, f2, eps)
while not (runge_rule(1 / 3, s1, s2, eps)):
    s1 = s2
    n2 *= 2
    s2 = trapezium_method(a, b, n2, f2, eps)
h = (b - a) / n2
print(s2, h, n2)

n2 = n1
s1 = parabola_method(a, b, n2, f2, eps)
n2 *= 2
s2 = parabola_method(a, b, n2, f2, eps)
while not (runge_rule(1 / 15, s1, s2, eps)):
    s1 = s2
    n2 *= 2
    s2 = parabola_method(a, b, n2, f2, eps)
h = (b - a) / n2
print(s2, h, n2)