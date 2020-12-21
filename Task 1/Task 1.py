#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, cos, pi
import matplotlib.pyplot as plt


def f1(x):
    return tan(x)


def f2(x):
    return 1 / (1 + 25 * pow(x, 2))


def f3(x):
    return abs(x)


def lagrange(x, y, t):
    s = 0
    for i in range(len(y)):
        p = 1
        for j in range(len(x)):
            if j != i:
                p *= (t - x[j]) / (x[i] - x[j])
        s += y[i] * p
    return s


l = [f1, f2, f3]

item = 0
while item != 1 and item != 2 and item != 3:
    print('Выберите функцию')
    print('1. tg(x)')
    print('2. 1/(1+25*x^2)')
    print('3. |x|')
    print('>>> ', end='')
    item = int(input())

f = l[item - 1]

a, b = -1, 1
n = int(input('n = '))

x = [a + 2 / 100 * k for k in range(101)]
y = [f(i) for i in x]  # функция

x1 = [a + k * (b - a) / (n - 1) for k in range(n)]  # равноотстоящие узлы
y1 = [f(i) for i in x1]

x2 = [a + 2 / 100 * k for k in range(101)]
y2 = [lagrange(x1, y1, i) for i in x2]  # Лагранж (равноотстоящие узлы)

x3 = [cos(((2 * k + 1) / (2 * n)) * pi) for k in range(n)]  # чебышевские узлы
y3 = [f(i) for i in x3]

x4 = [a + 2 / 100 * k for k in range(101)]
y4 = [lagrange(x3, y3, i) for i in x4]  # Лагранж (чебышевские узлы)

fig, ax = plt.subplots()
ax.plot(x, y, x2, y2, x4, y4)
ax.set_title('Графики функции и интерполяционного полинома Лагранжа')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(['Функция',
           'Лагранж (равноотстоящие узлы)', 'Лагранж (чебышевские узлы)'],
          loc='upper right', shadow=True)
plt.show()



#Входные данные:
#Выберите функцию
#1. tg(x)
#2. 1/(1+25*x^2)
#3. |x|
#»> 2
#n = 100