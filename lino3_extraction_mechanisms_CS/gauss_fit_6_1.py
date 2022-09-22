import matplotlib.pyplot as plt
import numpy as np 
from numpy import exp, loadtxt, pi, sqrt

from lmfit import Model

data = loadtxt('profile.dat')
x = data[:,0]
y = data[:,3]
x1 = data[150:, 0]
y1 = data[150:, 3]
a1 = max(y1)
b1= x1[y1.argmax()]
def gaussian(x1, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x1-cen)**2 / (2*wid**2))


gmodel = Model(gaussian)
result1 = gmodel.fit(y1, x1=x1, amp=0.1, cen=b1, wid=1)

print(result1.fit_report())


#plt.plot(x1, y1, 'bo')
#plt.plot(x1, result1.init_fit, 'k--')
#plt.plot(x1, result1.best_fit, 'r-')
#plt.show()

x2 = data[:150, 0]
y2 = data[:150, 3]
a2=max(y2)
b2 = x2[y2.argmax()]
def gaussian(x2, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x2-cen)**2 / (2*wid**2))


gmodel = Model(gaussian)
result2 = gmodel.fit(y2, x2=x2, amp=0.1, cen=b2, wid=1)

print(result2.fit_report())


#plt.plot(x2, y2, 'bo')
#plt.plot(x2, result2.init_fit, 'k--')
#plt.plot(x2, result2.best_fit, 'r-')
#plt.show()


plt.plot(x,y,'bo', x2, result2.best_fit, x1, result1.best_fit)
#plt.show() 
plt.savefig('gauss_fit.pdf')
plt.savefig('gauss_fit.jpeg', dpi= 92, facecolor='w', edgecolor='w',orientation='landscape', papertype=str, pad_inches=0.1, frameon=None, metadata=None)













