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
            oneDot = [float(line.split(" ")[0]), float(line.split(" ")[1])]
            dots.append(oneDot)
        else:
            nx.append(line)
    return 0

def get_four_dots(dots, x):
    for i in range (2, len(dots)):
        if x < dots[i][0] and x >= dots[i - 1][0]:
            return dots[i - 2], dots[i - 1], dots[i], dots[i + 1]

def calc_div_difference(pi, pj):
    y = (pi[1] - pj[1])/(pi[0] - pj[0])
    return y

#def substract(dots, x):
    #for i in range (len(dots)):



if __name__ == '__main__':
    dots = []
    nx = []
    get_input(dots, nx)
    n = int(nx[0])
    x = float(nx[1])
    nx = get_four_dots(dots, x)
    print(nx)
    print(calc_div_difference(nx[2], nx[3]))

