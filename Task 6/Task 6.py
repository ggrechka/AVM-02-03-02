#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def f1(x):
    return ((x + 1) ** 4) / 2


def f2(x, y):
    return (x + 1) ** 3 + 2 * y / (x + 1)


def runge_kutta_2_orders(f, x0, y0, n, h):
    x, y = [x0], [y0]
    for i in range(n):
        t = x[i] + h
        z = y[i] + h * f(x[i], y[i])
        x.append(t)
        y.append(y[i] + h * (f(x[i], y[i]) + f(t, z)) / 2)
    return x, y


def runge_kutta_4_orders(f, x0, y0, n, h):
    x, y = [x0], [y0]
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(x[i] + h / 2, y[i] + h * k3)
        x.append(x[i] + h)
        y.append(y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    return x, y


x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
n = int(input('n = '))
h = 1 / n

x = [h * i for i in range(n + 1)]
y = [f1(i) for i in x]
x1, y1 = runge_kutta_2_orders(f2, x0, y0, n, h)
x2, y2 = runge_kutta_4_orders(f2, x0, y0, n, h)

fig, ax = plt.subplots()

ax.plot(x, y, x1, y1, x2, y2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(['Точное решение', 'Метод Рунге-Кутта 2-го порядка', 'Метод Рунге-Кутта 4-го порядка'], loc='upper right',
          shadow=True)

plt.show()

#входные данные:
#x0 = 0
#y0 = 0.5
#n = 10
