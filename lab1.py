# Тема: Аппроксимация функций                                            #
# Программа вычисляет y(x) с помощью n-кратного полинома Ньютона         #
# ====================================================================== #
# Входные данные:        Результат:                                      #
# Таблица                Найти y(x) и сравнить с точным значением        #
# n                      Найти корень f(x) методом половинного деления   #
# x                      Найти корень f(x) методом обратной интерполяции #

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
    while (step < n + 1 and i < len(dots)):
        if x < dots[i][0] and x >= dots[i - 1][0]:
            if (step%2 != 0):
                d.append(dots[i])
                dots.pop(i)
            else:
                d.append(dots[i - 1])
                dots.pop(i - 1)
            i = 0
            step += 1
        i += 1
    for i in range (n - step):
        d.append(dots[i])
    d.sort()
    return d

def calc_div_difference(pi, pj, x):
    y = pi[2] + ((pj[2] - pi[2])*(x - pi[0]))/(pj[1] - pi[0])
    return y


def calc_polynomials(dots, x):
    diffs = []
    if (len(dots) == 2):
        return calc_div_difference(dots[0], dots[1], x)
    for i in range  (1, len(dots)):
        y = dots[i - 1][2]
        xi = dots[i - 1][0]
        xk = dots[i][1]
        diffs.append([xi, xk,
                      calc_div_difference(dots[i - 1], dots[i], x)])

    print(diffs)
    return calc_polynomials(diffs, x)


if __name__ == '__main__':
    list = []
    nx = []
    get_input(list, nx)
    n = int(nx[0])
    x = float(nx[1])
    dots = get_dots(list, x, n)
    print("*")
    print(dots)
    print("*")
    print("Ответ: " + str(calc_polynomials(dots, x)))

    #print(calc_div_difference(nx[2], nx[3]))

