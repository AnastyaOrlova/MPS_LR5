import math
import random

import matplotlib.pyplot as plt

masOfM = []
masOfD = []
masOfN = []
histX = []


def findV0(L, a):
    return math.sqrt(L * 9.8 / (math.sin(2 * math.radians(a))))


def findN(m, sigma):
    sum = 0
    for i in range(12):
        sum += random.random()
    sum -= 6
    N = m + sigma * sum
    return N


def findX(nV, nA):
    return math.pow(nV, 2) * (math.sin(2 * math.radians(nA))) / 9.8


def generateX(n, V, a, sigmaV, sigmaA):
    masOfX = []
    for i in range(n):
        nV = findN(V, sigmaV)
        nA = findN(a, sigmaA)
        X = findX(nV, nA)
        masOfX.append(X)
    return masOfX


def findM(n, masOfX):
    sum = 0
    for i in range(n):
        sum += masOfX[i]
    return sum / n


def findD(n, masOfX):
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += math.pow(masOfX[i], 2)
        sum2 += masOfX[i]
    sum2 = math.pow(sum2, 2) / n
    D = (sum1 - sum2) / (n - 1)
    return D


def getBins(L):
    bins = []
    for i in range(L - 110, L + 110, 5):
        bins.append(i)
    return bins


def findMas(n, V, a, sigmaV, sigmaA):
    global masOfM, masOfD, masOfN, histX
    for i in range(100, n + 100, 100):
        masOfX = generateX(i, V, a, sigmaV, sigmaA)
        masOfM.append(findM(i, masOfX))
        masOfD.append(findD(i, masOfX))
        masOfN.append(i)
        if (i == n):
            histX = masOfX

def getVariaty(L, delta, n):
    global histX
    number = 0
    for x in histX:
        if x < (L + delta / 2) and x > (L - delta / 2):
            number += 1
    return number / n


L = 1000
a = 50
V = findV0(L, a)
sigmaV = 1.5
sigmaA = 2
delta = 1

n = 5000
findMas(n, V, a, sigmaV, sigmaA)
bins = getBins(L)
variaty = getVariaty(L, delta, n)
print("Вероятность попадания в мишень:" + str(variaty))

fig, axs = plt.subplots(nrows=3, ncols=1)

fig.set_figwidth(10)
fig.set_figheight(10)
axs[0].grid(color='black',
            linewidth=1,
            linestyle='--')

axs[0].axis([100, n, min(masOfM) - 8, max(masOfM) + 8])
axs[0].plot(masOfN, masOfM, 'b', label='Мат ожидание', linewidth=2)
axs[0].legend(loc='upper right')

axs[1].grid(color='black',
            linewidth=1,
            linestyle='--')
axs[1].axis([100, n, min(masOfD) - 10, max(masOfD) + 10])
axs[1].plot(masOfN, masOfD, 'r', label='Дисперсия', linewidth=2)
axs[1].legend(loc='upper right')

axs[2].hist(histX, bins=bins, edgecolor='black')

plt.show()
