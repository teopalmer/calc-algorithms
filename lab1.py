# Тема: Аппроксимация функций                                            #
# Программа вычисляет y(x) с помощью n-кратного полинома Ньютона         #
# ====================================================================== #
# Входные данные:        Результат:                                      #
# Таблица                Найти y(x) и сравнить с точным значением        #
# n                      Найти корень f(x) методом половинного деления   #
# x                      Найти корень f(x) методом обратной интерполяции #
import math as m

def f(x, y):
    return x*y

def revert_dots(list):
    for a in list:
        temp = a[2]
        a[2] = a[0]
        a[1] = temp
        a[0] = temp

def float_array(line):
    d = []
    line = line.split(" ")
    for a in line:
        d.append(float(a))
    return d

def get_input(dots, inp):
    f = open("input.txt", 'r')
    for line in f:
        if line.find(" ") != -1:
            dots.append(float_array(line))
        else:
            inp.append(line)
    return 0

def get_base(arx, ary):
    dots = []
    for i in range(len(arx)):
        dots.append([arx[i], arx[i], ary[i]])
    return dots

def get_polbase(arx, ary):
    d = []
    for i in range(len(arx)):
        d.append([ary[i], ary[i], arx[i]])
    print(d)
    return d

def get_dots(list, x, n):
    dots = list
    d = []
    i = 0
    step = 0

    while step < n + 1 and i < len(dots):
        if dots[i][0] >= x >= dots[i - 1][0]:
            if step % 2 != 0:
                d.append(dots[i])
                dots.pop(i)
            else:
                d.append(dots[i - 1])
                dots.pop(i - 1)
            i = 0
            step += 1
        i += 1
    #print(dots)
    for i in range(n - step):
        if (i < len(dots)):
            d.append(dots[i])
        else:
            print("Слишком мало данных")
    d.sort()
    return d

def calc_div_diff(pi, pj, x):
    try:
        y = pi[2] + ((pj[2] - pi[2])*(x - pi[0]))/(pj[1] - pi[0])
        return y
    except ZeroDivisionError:
        return pi[2]

def calc_polynomials(dots, x):
    diffs = []

    if (len(dots)) == 1:
        print("Введена нулевая степень полинома")
        return 0

    if len(dots) == 2:
        return calc_div_diff(dots[0], dots[1], x)

    for i in range(1, len(dots)):
        y = dots[i - 1][2]
        xi = dots[i - 1][0]
        xk = dots[i][1]
        diffs.append([xi, xk,
                      calc_div_diff(dots[i - 1], dots[i], x)])

    return calc_polynomials(diffs, x)


if __name__ == '__main__':
    list = []
    inp = []
    pol = []
    get_input(list, inp)
    print("Введенные точки:")
    print(*list, sep="\n")
    ny, nx = int(inp[0]), int(inp[1])
    x, y = float(inp[2]), float(inp[3])
    arx, ary = list[0], list[1]

    for i in range(2, len(list)):
        base = get_base(arx, list[i])
        dots = get_dots(base, x, nx)
        pol.append(calc_polynomials(dots, x))

    d = get_polbase(pol, ary)
    d.sort()
    print(d)
    findots = get_dots(d, y, ny)
    cx = calc_polynomials(findots, y)
    print("Значение функции: {}".format(f(x, y)))
    print("Значение с помощью интерполяции: {}\n".format(cx))


