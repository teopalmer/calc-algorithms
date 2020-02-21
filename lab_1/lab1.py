# Тема: Аппроксимация функций                                            #
# Программа вычисляет y(x) с помощью n-кратного полинома Ньютона         #
# ====================================================================== #
# Входные данные:        Результат:                                      #
# Таблица                Найти y(x) и сравнить с точным значением        #
# n                      Найти корень f(x) методом половинного деления   #
# x                      Найти корень f(x) методом обратной интерполяции #
import math as m

def f(x):
    return x*x


def average(x, y):
    return (x + y)/2


def closeEnough(x, y, mid):
    if abs(x - y) < 0.01*abs(mid):
        return 1
    return 0


def search(f, negPoint, posPoint):
    midPoint = average(negPoint, posPoint)
    if closeEnough(negPoint, posPoint, midPoint):
        return midPoint
    testValue = calc_polynomials([negPoint, posPoint], x)
    if testValue > 0:
        return search(f, negPoint, midPoint)
    elif testValue < 0:
        return search(f, midPoint, posPoint)
    return midPoint


def halfIntervalMethod(a, b):
    aVal = f(a)
    bVal = f(b)
    if aVal > 0 and bVal < 0:
        return search(f, b, a)
    elif aVal < 0 and bVal > 0:
        return search(f, a, b)
    else:
        print("У аргументов не разные знаки")
        return 0


def revert_dots(list):
    for a in list:
        temp = a[2]
        a[2] = a[0]
        a[1] = temp
        a[0] = temp
    #print(list)


def get_input(dots, nx):
    f = open("input.txt", 'r')
    for line in f:
        if line.find(" ") != -1:
            oneDot = [float(line.split(" ")[0]),
                      float(line.split(" ")[0]),
                      float(line.split(" ")[1])]
            dots.append(oneDot)
        else:
            nx.append(line)
    return 0


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
    #x = (pj[1] - pi[0])/2
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
    nx = []
    get_input(list, nx)
    print("Введенные точки:")
    print(*list, sep="\n")
    n = int(nx[0])
    x = float(nx[1])
    hv = float(halfIntervalMethod(list[0][0], list[len(list) - 1][0]))
    dots = get_dots(list, x, n)

    print("\nИспользуемые точки: ", dots, '\n')
    print("Значение функции: {}".format(f(x)))
    print("Значение с помощью интерполяции: {}\n".format(calc_polynomials(dots, x)))
    print("Корень методом половинного деления: {}".format(hv))
    revert_dots(list)

    get_input(list, nx)
    revert_dots(list)
    list.sort()
    #print(list)
    dots = get_dots(list, 0, n)
    print("Корень с помощью интерполяции: ", calc_polynomials(dots, 0))

