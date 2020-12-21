#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import atan, sin, cos


def transpose(a):
    res = []
    n = len(a)
    for i in range(n):
        res.append([0] * n)
        for j in range(n):
            res[i][j] = a[j][i]
    return res


def mult(a, b):
    res = []
    n = len(a)
    for i in range(n):
        res.append([0] * n)
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res


def rotation(a, eps):
    '''
    Метод вращений.

    Ключевые аргументы:
    a - матрица
    eps - точность
    '''
    res = []
    n = len(a)  # nxn - размер матрицы a
    k = 0
    while True:
        i = j = mx = 0
        for l in range(n):
            for m in range(l + 1, n):
                if abs(a[l][m]) > mx:
                    i, j = l, m
                    mx = abs(a[l][m])
        if mx <= eps:
            break
        phi = atan(2 * a[i][j] / (a[i][i] - a[j][j])) / 2
        h = []
        for l in range(n):
            h.append([0] * n)
            h[l][l] = 1
        h[i][i] = h[j][j] = cos(phi)
        h[i][j] = -sin(phi)
        h[j][i] = sin(phi)
        a = mult(mult(transpose(h), a), h)  # (h^t *a) * h
        k += 1
        if n == 2:  # если матрица квадратная,  то одной итерации хватит(так сказали)
            break
    for i in range(n):
        res.append(a[i][i])  # гл.элементы а
    return res, k


a = []
f = open('input.txt', 'r')
eps = float(f.readline())
for line in f:
    line = line.strip()
    a.append(list(map(float, line.split())))
f.close()

res, k = rotation(a, eps)

f = open('output.txt', 'w')
f.write('Собственные числа:\n')
for i in range(len(a)):
    f.write(str(res[i]) + (' ' if i != (len(a) - 1) else '\n'))
f.write('Количество итераций: ' + str(k))
f.close()
