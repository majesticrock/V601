import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x +b


werte = csv_read("csv/messreihe2.csv")
xdata = np.zeros(21)
ydata = np.zeros(21)
ignore = True
i=0



for values in werte:
    if(i >= 21):
        break
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1])
        
        i+=1


x_line = np.linspace(0, 10.2)


plt.plot(xdata, ydata, 'r.', label="Energieverteilung")
#popt1, pcov1 = curve_fit(func, xdata, ydata)
#plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit")
plt.xlabel(r"$U_\text{A}$ / $\symup{V}$")
plt.ylabel(r"Steigung")
#print(popt1)
#print(np.sqrt(np.diag(pcov1)))
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("build/messreihe2.pdf")
