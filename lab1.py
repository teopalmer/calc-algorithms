# Тема: Аппроксимация функций                                            #
# Программа вычисляет y(x) с помощью n-кратного полинома Ньютона         #
# ====================================================================== #
# Входные данные:        Результат:                                      #
# Таблица                Найти y(x) и сравнить с точным значением        #
# n                      Найти корень f(x) методом половинного деления   #
# x                      Найти корень f(x) методом обратной интерполяции #
# Аппроксимация ф-и, восстановление ф-и по ее дискретному значению
# Многомерная интерполяция

from math import ceil

def f(x, y):
    return x ** 2 + y ** 2

def print_matrix(x, y, z):
    print("   y\\x ", end='')
    for i in x:
        print("{:6}".format(i), end=' ')

    for i in range(len(y)):
        print("\n{:6}".format(y[i]), end=' ')
        for j in z[i]:
            print("{:6}".format(j), end=' ')
    print('\n')

def get_matrix(x_0, x_step, x_n, y_0, y_step, y_n):
    x = [x_0 + i * x_step for i in range(x_n)]
    y = [y_0 + i * y_step for i in range(y_n)]
    z = [[f(i, j) for i in x] for j in y]
    return x, y, z

def get_matr(tbl, n):
    for i in range(n):
        tmp = []
        for j in range(n - i):
            tmp.append((tbl[i + 1][j] - tbl[i + 1][j + 1])
                       / (tbl[0][j] - tbl[0][i + j + 1]))
        tbl.append(tmp)
    return tbl

def get_dots(a, n, x):
    a_len = len(a)
    i_near = min(range(a_len), key=lambda i: abs(a[i] - x))
    space_needed = ceil(n / 2)

    if (i_near + space_needed + 1 > a_len):
        i_end = a_len
        i_start = a_len - n
    elif (i_near < space_needed):
        i_start = 0
        i_end = n
    else:
        i_start = i_near - space_needed + 1
        i_end = i_start + n

    return i_start, i_end


def interp_multi(x, y, z, x_val, y_val, x_n, y_n):
    ix_0, ix_end = get_dots(x, x_n + 1, x_val)
    iy_0, iy_end = get_dots(y, y_n + 1, y_val)

    x = x[ix_0: ix_end]
    y = y[iy_0: iy_end]
    z = z[iy_0: iy_end]
    for i in range(y_n + 1):
        z[i] = z[i][ix_0: ix_end]

    res = [interp_newt([x, z[i]], x_n, x_val)
           for i in range(y_n + 1)]
    return interp_newt([y, res], y_n, y_val)


def interp_newt(tbl, n, x):
    matr = get_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n + 1):
        res += tmp * matr[i + 1][0]
        tmp *= (x - matr[0][i])
    return res

if __name__ == '__main__':
    x_0 = float(input("X0: "))
    x_step = float(input("Step X: "))
    x_n = int(input("Number of dots: "))

    y_0 = float(input("Y0: "))
    y_step = float(input("Step Y: "))
    y_n = int(input("Number of dots: "))

    x, y, z = get_matrix(x_0, x_step, x_n, y_0, y_step, y_n)
    print("\nMatrix:")
    print_matrix(x, y, z)

    x_n = int(input("N(x): "))
    x_find = float(input("X: "))

    y_n = int(input("N(y): "))
    y_find = float(input("Y: "))

    found = interp_multi(x, y, z, x_find, y_find, x_n, y_n)
    print("\nInterpolated   : ", found)
    print("F(x, y)        : ", f(x_find, y_find))
