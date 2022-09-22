import sys
import numpy as np
#from dump import dump
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 

plt.style.use('classic')


### T300K
inputfile_300K = sys.argv[1]
infile_300K = open(inputfile_300K, 'r')
lines_300K = infile_300K.readlines()
lengthfile_300K = len(lines_300K)
infile_300K.close()
SurfTen_300K = []
Time = []
for i in range(25, lengthfile_300K):
    #if (lines[i].find('# Fix ') != -1):
    Time.append(float(lines_300K[i].split()[0]))
    SurfTen_300K.append(float(lines_300K[i].split()[1]))

### PLOTTING
NUM = len(Time)
conv_step = 50
conv_pont = int(NUM/conv_step)

sum_step_300K = []
for i in range(conv_pont):
    
    sum_step_300K.append((i*conv_step, np.mean(SurfTen_300K[:i*conv_step])/20.))
    

sum_step_300K = np.array(sum_step_300K)

plt.plot(sum_step_300K[:, 0], sum_step_300K[:, 1], label='T=298K', color='green', linewidth=1.0)

plt.legend(loc='lower right', fontsize=14)
plt.xlabel(r'Time (ps)', fontsize=12)
plt.ylabel(r'r (mN/m)', fontsize=12)
#plt.ylim(2, 23)
#plt.xlim(230, 350)
plt.savefig('SurfTens_Converge_Temp298.pdf', bbox_inches='tight', ppi=1200)
np.savetxt('SurfTens_Converge_Temp298.csv', np.column_stack((sum_step_300K[:, 0], sum_step_300K[:, 1])))
"""
print "average value of interfacial tension"
print X_av, Y_av, WAT_av, TRIBP_av, MainWAT_av, ExtWAT_av

#ax = plt.figure().gca() 
#ax.yaxis.set_major_locator(MaxNLocator(integer=True))

fig, left_axis = plt.subplots()
right_axis = left_axis.twinx()

left_axis.errorbar(N, X, yerr=Y, fmt='.-', label='$Interface Tension$', color="red", linewidth=1.)
#left_axis.plot(N, X, '.-', label='Interfacial Tension', color="blue", linewidth=1.)
right_axis.plot(N, TRIBP, '*-', label='$N_{TBP}$', color="black", linewidth=1.)

left_axis.set_xlabel(r'$T{}$ (K)', fontsize=14)
left_axis.set_ylabel(r'$r{} (mN/m)$', fontsize=14)
right_axis.set_ylabel('Interfacial TBP', fontsize=13)

left_axis.set_xlim(230, 350)
left_axis.set_ylim(5, 35)
right_axis.set_ylim(180, 270)

#ax.plot(N, X, '.-', label='Interfacial Tension', color="blue", linewidth=1.)
#ax.errorbar(N, X, yerr=Y, fmt='.-', color="red", linewidth=1.)
#ax.plot(N, WAT, 'v-', label='$N_{water}$', color="blue", linewidth=1.)
#ax.plot(N, MainWAT, '^-', label='$N_{interfacial-water}$', color="lightblue", linewidth=1.)
#ax.plot(N, ExtWAT, '+-', label='$N_{extracted-water}$', color="blue", linewidth=1.)
#ax.plot(N, TRIBP, '*-', label='$N_{TBP}$', color="black", linewidth=1.)
#ax.set_xlabel(r'$T{}$ (K)')
#ax.set_ylabel(r'$r{} (mN/m)$', fontsize=14)
plt.legend(loc="upper right")
#plt.ylim(2, 23)
#plt.xlim(230, 350)
plt.savefig('SurfTen_TBPconcent.pdf', bbox_inches='tight', ppi=1200)
"""
