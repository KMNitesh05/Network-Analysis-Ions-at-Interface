####### Author : Nitesh KM ########

####### Graduate Student : Washington State University #######

##### Convergence of Energy ########

import sys
import numpy as np
#from dump import dump
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 

plt.style.use('classic')

### T=300K
inputfile_300K = sys.argv[1]
infile_300K = open(inputfile_300K, 'r')
lines_300K =  infile_300K.readlines()
lengthfile_300K = len(lines_300K)
infile_300K.close()
Time = []
TotEnergy_300K = []
for i in range(26, lengthfile_300K):
    #if (lines[i].find('# Fix ') != -1):
    Time.append(float(lines_300K[i].split()[0]))
    TotEnergy_300K.append(float(lines_300K[i].split()[1]))

### PLOTTING
NUM = len(Time)
conv_step = 50
conv_pont = NUM/conv_step

sum_step_300K = []
for i in range(conv_pont):
	sum_step_300K.append((i*conv_step, np.mean(TotEnergy_300K[:i*conv_step])/20.))


np.save(sum_step_300K)

sum_step_300K = np.array(sum_step_300K)
plt.plot(sum_step_300K[:, 0], sum_step_300K[:, 1], label='T=300K', color='red', linewidth=1.0)
plt.legend(loc='lower right', fontsize=14)
plt.xlabel(r'Time (ps)', fontsize=12)
plt.ylabel(r'E (KJ/mol)', fontsize=12)
#plt.ylim(2, 23)
#plt.xlim(230, 350)
plt.savefig('TE_Converge_Temp.pdf', bbox_inches='tight', ppi=1200)





