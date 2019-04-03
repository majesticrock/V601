import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
X = [25.5 + 273.15, 143 +273.15, 195.5 + 273.15, 106 + 273.15] #K
err = [0.1, 0.1, 0.1, 0.1]
T = unp.uarray(X, err)
a = 0.01 #m
i = 0
for x in T:
    p = 5.5 * 10**7 * unp.exp(-6876/T[i])
    w = 0.0029/p * 10**(-2)
    r = a / w
    print(T[i], w, r)
    i = i+1 
print(0.1  * 0.000029/(6876* 5.5 * 10**7 * np.exp(-6876/298.65)/298.65**2))




####Traegheitsmoment
#rk = 0.02615 #m
#mk = 0.14197 #kg
#jk = 2/5 * mk * rk**2
#print(jk)
#R = 0.109
#d = 0.138
#N = 195
#
#def csv_read(pathToFile, delimiter=";"):
#    with open(pathToFile, "r") as f:
#        content = []
#        for line in f:
#            content.append((line.rstrip()).split(delimiter))
#    return content
#def func(x, a, b):
#    return a*x + b
#werte = csv_read("csv/gravi.csv")
#data0 = np.zeros(10)
#data1 = np.zeros(10)
#B = np.zeros(10)
#ignore = True
#i=0
#
#for values in werte:
#    if(ignore):
#        ignore = False
#    else:
#        data0[i] = float(values[0])
#        data1[i] = float(values[1])
#        data1[i] = data1[i] + 0.01225 + 0.02615
#        B[i] = (4*np.pi*10**(-7) * data0[i] * R**2) / (R**2 + (d/2)**2)**(3/2)
#        print(data0[i])
#        print(data1[i])
#        print(B[i])
#        i = i+1
#
#xdata = data1
#ydata = B
#x_line = np.linspace(0, 6)
#plt.plot(xdata, ydata, 'bx', label="Wertepaare")
#popt1, pcov1 = curve_fit(func, xdata, ydata)
#plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")
#print(popt1)
##print(np.diag(np.sqrt(pcov1)))
#plt.legend()
#plt.tight_layout()
#plt.savefig("build/gravitation.pdf")