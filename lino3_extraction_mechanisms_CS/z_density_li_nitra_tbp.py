import sys
import numpy as np
#from dump import dump
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 
plt.style.use('classic')
#import plotly.plotly as py
#import plotly.tools as tls
import os, sys

print ("molecule_name, start_snap, end_snap, deltaT")
print ("eg. WATER/OCTA_OH, 0, 10000, 2")


n = 7055 
time_b = int(sys.argv[1])  #0
time_e = int(sys.argv[2])  #10000
delta_t = int(sys.argv[3]) #1
t= time_b
amsum = []

while t <= time_e:
    x = []
    tbp_cnt = []         
    nitra_cnt = []            
    with open('Li_TRIBP4HBonding' + str(t) + '.input.' + "li" + str(t) + '.xyz.' + 'O_TBP' + str(t) + '.xyz.' + 'GraphGeod','r') as inputfile:
        print(t)
        lines = inputfile.readlines()
        lengthfile = len(lines)
        inputfile.close()
        edge_u = []
        #edge_u2 = []
        for i in range(0, lengthfile):
            #if (lines[i].find('# Fix ') != -1):
            edge_u.append(int(lines[i].split()[0]))
        for i in range(0,700 ,1): 
        #if i in x: 
            print(i)
            cnt = edge_u.count(i)
            if cnt == 2 : 
                tbp_cnt.append(i)
            #edge_u2.append(int(lines[i].split()[0]))
        print(edge_u)
        #printMatrix(adjMatrix)                       
    with open('nitra_li' + str(t) + '.input.' + 'nitra' + str(t) + '.xyz.' + 'li' + str(t) + '.xyz.' + 'GraphGeod','r') as inputfile1:
        print(t)
        lines1 = inputfile1.readlines()
        lengthfile1 = len(lines1)
        inputfile1.close()
        edge_u1 = []
        for i in range(0, lengthfile1):
            if int(lines1[i].split()[5]) == 4 :
                edge_u1.append(int(lines1[i].split()[0]))
            #edge_u2.append(int(lines[i].split()[0]))
        #print("Adjacency matrix: ")
        print(edge_u1)
        #printMatrix(adjMatrix) 
        for i in range(0,700 ,1): 
            #if i in x: 
                print(i)
                cnt1 = edge_u1.count(i)
                if cnt1 == 2 : 
                    nitra_cnt.append(i)
    #print(zero_hb)
    with open('li' + str(t)  + '.gro') as inputfile2:
        #print(t)
        lines2 = inputfile2.readlines()
        lengthfile2 = len(lines2)
        inputfile2.close()
        for i in range(2,lengthfile2-1):
            #if (str(lines[i].split()[:-5]) == 'O2') :
                if (int(lines2[i].split()[0][:4])-7205) in tbp_cnt : 
                    if (int(lines2[i].split()[0][:4])-7205) in nitra_cnt :
                        amsum.append((float((float(lines2[i].split()[-1])))))

                else :
                    pass                                    
        

    t += delta_t
print(amsum)

#hist1 = []
#bins1 = []
#num_bins = 20
#hist,bins,n = plt.hist(amsum, facecolor='blue', alpha=0.5, density = True)
#for i in xrange(0,len(hist)):
    #hist1.append(hist[i])
    #bins1.append(bins[i])


#plt.savefig('wat_wat_amsum_bulk.pdf', bbox_inches='tight', ppi=1200)
np.savetxt('li_2no3_2tbp_adsorbed_z_distribution.csv',amsum)
#np.savetxt('wat_wat_hist_bulk.csv',np.column_stack((hist1, bins1)))

























    
    
    
    


 


    
    









#sum_rows = np.sum(adjMatrix , axis=1)


    

   

#np.savetxt('amsum.csv',amsum)




















### PLOTTING
#NUM = len(Time)
#conv_step = 50
#conv_pont = NUM/conv_step

#sum_step_300K = []
#for i in xrange(conv_pont):
    
    #sum_step_300K.append((i*conv_step, np.mean(SurfTen_300K[:i*conv_step])/20.))
    

#sum_step_300K = np.array(sum_step_300K)

#plt.plot(sum_step_300K[:, 0], sum_step_300K[:, 1], label='T=300K', color='green', linewidth=1.0)

#plt.legend(loc='lower right', fontsize=14)
#plt.xlabel(r'Time (ps)', fontsize=12)
#plt.ylabel(r'r (mN/m)', fontsize=12)
#plt.ylim(2, 23)
#plt.xlim(230, 350)
#plt.savefig('SurfTens_Converge_Temp300.pdf', bbox_inches='tight', ppi=1200)

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
