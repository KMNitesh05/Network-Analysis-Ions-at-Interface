"""
=============================
Making Histograms NITESH KM 
=============================

"""
import numpy as np
from scipy.special import erf
from scipy import special
from scipy.optimize import curve_fit
from pylab import *
import matplotlib.pyplot as plt
from numpy import loadtxt, pi, sqrt
import math 
from lmfit import Minimizer, Parameters, report_fit

x1 = []
y1 = []


with open('density_water_mass.xvg','r') as inputfile:
    #print(t)
    lines = inputfile.readlines()
    lengthfile = len(lines)
    inputfile.close()
    for i in range(2, 20):
        x1.append(float(lines[i].split()[0]))
        y1.append(float(lines[i].split()[1]))


x1 = np.array(x1)
#x1 = x1/x1[0] #x1 = x1/(np.sum(x1))
y1 = np.array(y1)
y1 = np.mean(y1)


print(y1)
#hist2 = [x / a for x in hist1]
#np.savetxt('bulk_org_dens_lino.csv',np.column_stack((y1, x1)))

#bins=np.arange(-1.2,1.2,0.2)








