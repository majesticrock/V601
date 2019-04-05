import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

werte = csv_read("csv/franck.csv")
xdata = np.zeros(8)
ydata = np.zeros(8)
ignore = True
i=0



for values in werte:
    if(i >= 8):
        break
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1])
        
        i+=1

print(np.mean(ydata))
print(np.std(ydata, ddof=1) / np.sqrt(len(ydata)))
a = ufloat(np.mean(ydata), np.std(ydata, ddof=1) / np.sqrt(len(ydata)) )

h = 4.135667662e-15
c = 299792458

print(c * h/(a))
print(c/(a**2/h) * 0.11301765822838729 ) 
