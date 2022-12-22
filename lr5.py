import math
import random

from matplotlib import pyplot as plt

ma = 45 #угол стрельбы
L = 1000 #растояние(длина выстрела)
g = 10 #ускорение
z = 5000 # количество итераций
mv = math.sqrt(L * g / (math.sin(2 * math.radians(ma)))) # начальная скорость, мат ожидание v
#print (mv)
sv = 1.5 # среднквадр. откл. для скорости
sa = 1.5 # среднквадр. откл. для угла
delt = 10

MasV = [] # массив скорости
MasA = [] # массив углов
MasX = [] # массив расстояний
MasM = [] # массив мат ожид
MasD = [] # масив дисп
MasN = []
hist_x = []
Sum = 0
for i in range (z):
    r = 0
    for i in range (12):  # создание рандомных v и перевод из равн в норм закон
        R = random.uniform(0,1)
        r = r + R
    N = r - 6
    Nv = mv + sv * N
    MasV.append(Nv)
    r = 0
    for i in range (12): # создание рандомных a и перевод из равн в норм закон
        R = random.uniform(0,1)
        r = r + R
    N = r - 6
    Na = ma + sa * N
    MasA.append(Na)

    X = math.pow(Nv, 2) * (math.sin(2 * math.radians(Na))) / g # расчет X и запись в массив
    Sum += X
    Q = X/z
    hist_x.append(Q)
    MasX.append(X)

Sr = Sum/z # среднее значение X

def M(z, MasX):  # расчет мат ожид
    sm = 0
    for i in range(z):
        sm += MasX[i]
    M = sm / z
    return M

def D(z, MasX): # расчет дисп
    s1 = 0
    s2 = 0
    for i in range(z):
        s1 += math.pow(MasX[i], 2)
        s2 += MasX[i]
    s2 = math.pow(s2, 2) / z
    D = (s1 - s2) / (z - 1)
    return D

def Mas(z): # создание значений для графиков
    global MasM, MasD, MasN, X
    for i in range(100, z + 100, 100):
        MasM.append(M(i, MasX))
        MasD.append(D(i, MasX))
        MasN.append(i)
        if (i == z):
           X = MasX

Mas(z)
sm = 0
D = D(z, MasX)
print("D = ", D)
sigma = math.sqrt(D)
print("sigma = ", sigma)
M = M(z, MasX)
print("M = ", M)
number = 0
p = 0
for x in MasX: # расчет вероятности попадания в мишень
    if x < (L + delt / 2) and x > (L - delt / 2):
        number += 1
        p = number / z

#SIG = (1 / (sigma * math.sqrt(2 * math.pi))) * math.pow(math.e, math.pow(x - M, 2)) / (2 * (math.pow(sigma, 2))) #############
#print("SIG = ", SIG)
MasDel = []
for i in range(L - 100, L + 100, 2): # значения для гистограммы
    MasDel.append(i)

#print(MasDel)
print("p = ", p)
#print("X = ", X)
#print("Sum = ", Sum)
#print("Sr = ", Sr)
#print("MasV = ", MasV)
#print("MasA = ", MasA)
#print("MasX = ", MasX)


#print("MasM = ", MasM)
#print("MasD = ", MasD)
#print("MasN = ", MasN)

fig, axs = plt.subplots(nrows = 3, ncols = 1)

fig.set_figwidth(10)
fig.set_figheight(10)

axs[0].axis([100, z, min(MasM) - 3, max(MasM) + 3]) # график зависимости мат ожид от числа исп
axs[0].plot(MasN, MasM, label = 'Мат ожидание', linewidth = 2)
axs[0].legend(loc='upper right')

axs[1].axis([100, z, min(MasD) - 5, max(MasD) + 5]) # график зависимости дисп от числа исп
axs[1].plot(MasN, MasD, label = 'Дисперсия', linewidth = 2)
axs[1].legend(loc = 'upper right')

axs[2].hist(X, bins = MasDel, edgecolor = 'black') # гистограмма

plt.show()




