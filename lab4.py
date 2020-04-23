import matplotlib.pyplot as plt
import numpy as np

screen_color = "#FFDFFE"
dot_color = "#058B4D"
line_color = "#CD165F"

def f(dots, c):
    res = [0.] * dots
    for i in range(len(c)):
        res += c[i] * (dots ** i)
    return res

# Считать данные с файла
def read_file(filename):
    f = open(filename, "r+")
    x, y, weight = [], [], []
    for s in f:
        s = s.split(" ")
        x.append(float(s[0]))
        y.append(float(s[1]))
        weight.append(float(s[2]))
    f.close()
    return x, y, weight


def print_table(x, y, weight):
    print("x      y      weight")
    for i in range(len(x)):
        print("%.4f %.4f %.4f" % (x[i], y[i], weight[i]))
    print()


def print_mtr(mtr):
    for i in mtr:
        print(i)


# методом Гаусса
def solve_mtr(mtr):
    l = len(mtr)

    for k in range(l):
        for i in range(k + 1, l):
            t = - (mtr[i][k] / mtr[k][k])
            for j in range(k, l + 1):
                mtr[i][j] += t * mtr[k][j]

    c = [0 for i in range(l)]

    for i in range(l - 1, -1, -1):
        for j in range(l - 1, i, -1):
            mtr[i][l] -= c[j] * mtr[i][j]
        c[i] = mtr[i][l] / mtr[i][i]
    return c

def make_mtr(x, y, weight, n, N):
    mtr = [[0 for y in range(n + 2)] for x in range(n + 1)]
    for k in range(n + 1):
        for i in range(n + 1):
            sum_x = 0
            for j in range(len(x)):
                sum_x += x[j] ** (i + k) * weight[j]
            mtr[k][i] = round(sum_x, 4)
        s = 0
        if k != 0:
            for j in range(len(x)):
                s += y[j] * x[j] ** k * weight[j]
        else:
            for j in range(len(y)):
                s += y[j] * weight[j]
        mtr[k][n + 1] = round(s, 4)
    print("MATRIX\n")
    print_mtr(mtr)
    c = solve_mtr(mtr)
    print("\nCOEFFICIENTS\n\n", c)
    print("\nAPPROXIMATION FUNCTION\n\nF = ", round(c[0], 2), sep="", end="")
    for i in range(1, len(c)):
        print(" + (", round(c[i], 2), ") * x ** ", i, sep="", end="")
    return c

def make_plot(c, x, y, weight, dots):
    plt.figure(1, facecolor=screen_color)
    plt.plot(dots, f(dots, c), color=line_color)
    plt.ylabel("Y")
    plt.xlabel("X")
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'ro', markersize=weight[i] + 2, color=dot_color)
    plt.show()

if __name__ == '__main__':
    x, y, weight = read_file("dots.txt")
    N = len(x) - 1 # количество узлов
    n = int(input("Enter the degree of the polynomial: "))
    print("n = ", n, " N = ", N)
    print_table(x, y, weight)
    c = make_mtr(x, y, weight, n, N)
    dots = np.arange(x[0] - 2, x[len(x) - 1] + 2, 0.01)
    make_plot(c, x, y, weight, dots)


