import math
import random
import matplotlib.pyplot as plt
import numpy


def normal(m, s):
    r = 0
    for i in range(6):
        r = r + random.uniform(0, 1)
    n = m + (s * (r - 6))
    return n


def shot(m_v, s_v, m_a, s_a):
    v = normal(m_v, s_v)
    a = normal(m_a, s_a)
    x = v ** 2 * (math.sin(2 * math.radians(a))) / 9.8
    return x


def calc_m(x_array):
    sm = 0
    shot_count = len(x_array)
    for i in range(shot_count):
        sm += x_array[i]
    m = sm / shot_count
    return m


def calc_d(x_array):
    s1 = 0
    s2 = 0
    shot_count = len(x_array)
    for i in range(shot_count):
        s1 += x_array[i] ** 2
        s2 += x_array[i]
    s2 = math.pow(s2, 2) / shot_count
    d = (s1 - s2) / (shot_count - 1)
    return d


def calc_p(l, delta, hist_x):
    shot_count = len(hist_x)
    number = 0
    for x in hist_x:
        if (l + delta / 2) > x > (l - delta / 2):
            number += 1
    return number / shot_count


def check_percent(x_array):
    m = calc_m(x_array)
    d = calc_d(x_array)
    m_plus = m + 3 * math.sqrt(d)
    m_minus = m - 3 * math.sqrt(d)
    x_count = 0
    for x in (x_array):
        if m_plus > x > m_minus:
            x_count += 1

    x_percent = x_count / len(x_array) * 100
    return x_percent


if __name__ == '__main__':
    shot_count = 5000
    l = 1000
    delta = 50
    m_v = 104.699
    m_a = 45
    s_v = 1.5
    s_a = 1.5

    x_array = []
    for i in range(shot_count):
        x_array.append(shot(m_v, s_v, m_a, s_a))

    d = calc_d(x_array)
    print(d)
    print(calc_m(x_array))
    print(calc_p(l, delta, x_array))
    print(check_percent(x_array))
    fig, axs = plt.subplots(nrows=3, ncols=1)

    fig.set_figwidth(10)
    fig.set_figheight(10)

    mas_m = []
    mas_d = []
    mas_i = []

    for i in range(100, shot_count + 100, 100):
        x_array = []
        for j in range(shot_count):
            x_array.append(shot(m_v, s_v, m_a, s_a))
        mas_m.append(calc_m(x_array))
        mas_d.append(calc_d(x_array))
        mas_i.append(i)

    axs[0].plot(mas_i, mas_m, label='Мат ожидание', linewidth=2)
    axs[0].legend(loc='upper right')

    axs[1].axis([100, shot_count, min(mas_d) - 5, max(mas_d) + 5])
    axs[1].plot(mas_i, mas_d, label='Дисперсия', linewidth=2)
    axs[1].legend(loc='upper right')

    axs[2].hist(x_array, bins=20, edgecolor='black', density=True)  # гистограмма

    plt.show()
