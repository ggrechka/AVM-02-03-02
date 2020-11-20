#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy

def is_symmetrical(n, a):
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] != a[j][i]:
                return False
    return True

def det(n, a):
    if n == 1:
        return a[0][0]
    s = 0
    for j in range(n):
        m = deepcopy(a)
        del m[0]
        for i in range(n - 1):
            del m[i][j]
        s += (-1) ** j * a[0][j] * det(n - 1, m)
    return s

def sylvester_test(n, a):
    for i in range(1, n + 1):
        m = deepcopy(a)
        for j in range(n):
            for k in range(n - 1, i - 1, -1):
                del m[j][k]
        for j in range(n - 1, i - 1, -1):
            del m[j]
        if det(i, m) <= 0:
            return False
    return True

def cholesky_method(n, a, f):
    # вычисление элементов матрицы L
    l = deepcopy(a)
    l[0][0] = a[0][0] ** 0.5
    for j in range(1, n):
        l[j][0] = a[j][0] / l[0][0]
    for i in range(1, n):
        s = 0
        for p in range(0, i):
            s += l[i][p] ** 2
        l[i][i] = (a[i][i] - s) ** 0.5       
        for j in range(i + 1, n):
            s = 0
            for p in range(0, i):
                s += l[i][p] * l[j][p]
            l[j][i] = (a[j][i] - s) / l[i][i]
    # решение уравнения L * y = f
    y = [0] * n
    for i in range(n):
        s = 0
        for j in range(0, i):
            s += l[i][j] * y[j]
        y[i] = (f[i] - s) / l[i][i]
    # решение уравнения L^T * x = y
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i, n):
            s += l[j][i] * x[j]
        x[i] = (y[i] - s) / l[i][i]
    return x
    
def mult(n, a, b):
    c = [0] * n
    for i in range(n):
        for j in range(n):
            c[i] += a[i][j] * b[j]
    return c

f = open('input.txt', 'r')
line = f.readline()
n = int(line.strip())
a, f1 = [], []
for i in range(n):
    line = f.readline()
    line = line.split()
    a.append(list(map(float, line[:n])))
    f1.append(float(line[n]))
f.close()

b1 = is_symmetrical(n, a)
b2 = sylvester_test(n, a)
f = open('output.txt', 'w')
if b1 and b2:
    x = cholesky_method(n, a, f1)
    f2 = mult(n, a, x)
    f.write('Решение:\n')
    f.write(' '.join(list(map(str, x))) + '\n')
    f.write('Вектор невязки:\n')
    for i in range(n - 1):
        f.write(str(f2[i] - f1[i]) + ' ')
    f.write(str(f2[n - 1] - f1[n - 1]) + '\n')
elif b1 and not(b2):
    f.write('Матрица не является положительно-определённой')
elif not(b1) and b2:
    f.write('Матрица не является симметричной')
else:
    f.write('Матрица не является симметричной и положительно-определённой')
f.close()