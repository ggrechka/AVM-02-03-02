#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, pi

func = [lambda x: 2 * x ** 2,
        lambda x: 8 + 2 * x - x ** 2,
        lambda x: sin(x) / (cos(x) ** 2 + 1)]


def select_function_number():
    print("Список доступных функций:\n 1.2 * x ^ 2 \n 2.8 + 2 * x - x ^ 2 \n 3.sin(x) / (cos(x) ^ 2 + 1)")
    number = int(input("Выберите номер функции: "))
    while number not in [1, 2, 3]:
        number = int(input("Номер функции некорректный, попробуйте снова: "))
    return number - 1


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


print("|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|")
a = float(input('Введите левую границу a = '))
b = float(input('Введите правую границу b = '))
n1 = int(input('Введите количество разбиений = '))
eps = float(input('Введите точность eps = '))
print("|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|")
number = select_function_number()

n2 = n1
s1 = trapezium_method(a, b, n2, func[number], eps)
n2 *= 2
s2 = trapezium_method(a, b, n2, func[number], eps)
while not (runge_rule(1 / 3, s1, s2, eps)):
    s1 = s2
    n2 *= 2
    s2 = trapezium_method(a, b, n2, func[number], eps)
h = (b - a) / n2
print("Метод трапеций: \n","Итоговое значение: ", s2, "\n", "Длина разбиения:", h, "\n", "Количество разбиений:  ", n2, "\n")

n2 = n1
s1 = parabola_method(a, b, n2, func[number], eps)
n2 *= 2
s2 = parabola_method(a, b, n2, func[number], eps)
while not (runge_rule(1 / 15, s1, s2, eps)):
    s1 = s2
    n2 *= 2
    s2 = parabola_method(a, b, n2, func[number], eps)
h = (b - a) / n2
print("Метод Симпсона: \n", "Итоговое значение: ", s2, "\n", "Длина разбиения:", h, "\n", "Количество разбиений:  ", n2, "\n")
