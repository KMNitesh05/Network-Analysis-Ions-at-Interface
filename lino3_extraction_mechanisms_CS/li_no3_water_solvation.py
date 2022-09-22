import os, sys
import numpy as np 
import os, sys
import pandas as pd 

print ("molecule_name, start_snap, end_snap, deltaT")
print ("eg. WATER/OCTA_OH, 0, 10000, 2")


time_b = int(sys.argv[1])  #0
time_e = int(sys.argv[2])  #10000
delta_t = int(sys.argv[3]) #1
amsum = []
amsum2 = []
amsum3 = []
t= time_b
while t <= time_e:
    y = []
    x = []
    with open('/Volumes/RAM_ECC/WAT_HEX_TBP_IONS/LINO3_project/LINO_TBP_10_90/5m/analysis/itim/ion_layer_pdb' + str(t)  + '.pdb') as inputfile:
        #print(t)
        lines = inputfile.readlines()
        lengthfile = len(lines)
        inputfile.close()    
        for i in range(2,lengthfile-1,1):
            if (str(lines[i].split()[-1]) == 'SYSTLI' ) and (float(lines[i].split()[9]) == 1.00 ):
                m = int((lines[i].split()[4][1:]))-7205
                y.append(m)
                print(y)

            else:
                pass       
        #print (y)         
    with open('/Volumes/RAM_ECC/WAT_HEX_TBP_IONS/LINO3_project/LINO_TBP_10_90/5m/analysis/itim/water_li_1solvation' + str(t) + '.input.' + 'li' + str(t) + '.xyz.' + 'wat' + str(t) + '.xyz.' + 'Graph','r') as inputfile1:
        #print(t)
        lines1 = inputfile1.readlines()
        lengthfile1 = len(lines1)
        inputfile1.close()
        edge_u = []
        for i in range(0, lengthfile1):
            #if (lines[i].find('# Fix ') != -1):
            edge_u.append(int(lines1[i].split()[0]))

    with open('nitra_li' + str(t) + '.input.' + 'nitra' + str(t) + '.xyz.' + 'li' + str(t) + '.xyz.' + 'GraphGeod','r') as inputfile2:
        #print(t)
        lines2 = inputfile2.readlines()
        lengthfile2 = len(lines2)
        inputfile2.close()
        edge_u2 = []
        for i in range(0, lengthfile2):
            print(int(lines2[i].split()[5]))
            #if int(lines1[i].split()[0]) in x : 
                #print (int(lines1[i].split()[0]))

            if (int(lines2[i].split()[5]) == 4 ) :
                #if (lines[i].find('# Fix ') != -1):
                edge_u2.append(int(lines2[i].split()[0]))

        #print (edge_u2)    
        #print("Adjacency matrix: ")
        #printMatrix(adjMatrix) 
        #print(edge_u) 
        for j in range(1,650): 
            if j in edge_u :  
                #if j in edge_u : 
                #print(j)
                cnt = edge_u.count(j)
                amsum.append(cnt)
                cnt2 = edge_u2.count(j)
                amsum2.append(cnt2)
    t += delta_t


#b = []
#print (len(amsum))
#a = len(amsum)/time_e
#b.append(np.mean(amsum)*time_e/len(amsum))
#print(amsum)

df = pd.DataFrame({'one': pd.Series(amsum2),'two':pd.Series(amsum)})    
amsum3.append(df.groupby(df.columns.tolist(),as_index=False).size())
    
print (amsum3)

np.savetxt('li_nitra_water_solvation_layer1_list.csv',np.column_stack((amsum, amsum2)))
np.savetxt('li_nitra_water_solvation_layer1.csv',amsum3)









