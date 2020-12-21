#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from copy import copy
import matplotlib.pyplot as plt


def jacobi(eps, n, a, b, x):
    '''
    Метод Якоби.

    Ключевые аргументы:
    eps - желаемая точность;
    n - размер матрицы;
    a[n][n] - матрица коэффициентов;
    b[n] - столбец свободных членов;
    x[n] - начальное приближение, ответ записываетс¤ также в x[n].
    '''
    temp_x = [0] * n
    m = 0
    l = []
    f = True
    while f:
        for i in range(n):
            temp_x[i] = b[i]
            for j in range(n):
                if j != i:
                    temp_x[i] -= a[i][j] * x[j];
            temp_x[i] /= a[i][i]
        norm = 0
        for i in range(n):
            norm += pow(x[i] - temp_x[i], 2)
            x[i] = temp_x[i]
        m += 1
        l.append((m, norm))
        f = sqrt(norm) > eps
    return l, x


def seidel(eps, n, a, b, x):
    '''
    Метод Зейделя.

    Ключевые аргументы:
    eps - желаемая точность;
    n - размер матрицы;
    a[n][n] - матрица коэффициентов;
    b[n] - столбец свободных членов;
    x[n] - начальное приближение, ответ записываетс¤ также в x[n].
    '''
    temp_x = [0] * n
    m = 0
    l = []
    f = True
    while f:
        for i in range(n):
            temp_x[i] = x[i]
        for i in range(n):
            var = 0
            for j in range(i):
                var += (a[i][j] * x[j])
            for j in range(i + 1, n):
                var += (a[i][j] * temp_x[j])
            x[i] = (b[i] - var) / a[i][i]
        norm = 0
        for i in range(n):
            norm += pow(x[i] - temp_x[i], 2)
        m += 1
        l.append((m, norm))
        f = sqrt(norm) > eps
    return l, x


f = open('input.txt', 'r')
n = int(f.readline())
eps = float(f.readline())
a = [0] * n
b = [0] * n
for i in range(n):
    line = f.readline().split()
    a[i] = list(map(float, line[:len(line) - 1]))
    b[i] = float(line[len(line) - 1])
x1 = list(map(float, f.readline().split()))
x2 = copy(x1)
f.close()

v1, x3 = jacobi(eps, n, a, b, x1)

f = open('output1.txt', 'w')
f.write('Решение:\n')
f.write((' '.join(list(map(str, x3))) + '\n'))
f.close()

v2, x4 = seidel(eps, n, a, b, x2)

f = open('output2.txt', 'w')
f.write('Решение:\n')
f.write((' '.join(list(map(str, x4))) + '\n'))
f.close()

x1 = [v1[i][0] for i in range(len(v1))]
y1 = [v1[i][1] for i in range(len(v1))]
x2 = [v2[i][0] for i in range(len(v2))]
y2 = [v2[i][1] for i in range(len(v2))]

fig, ax = plt.subplots()

ax.plot(x1, y1, x2, y2)
ax.set_xlabel('Номер итерации')
ax.set_ylabel('Норма невязки')
ax.grid(True)
ax.legend(['Метод Якоби', 'Метод Зейделя'], loc='upper right', shadow=True)

plt.show()