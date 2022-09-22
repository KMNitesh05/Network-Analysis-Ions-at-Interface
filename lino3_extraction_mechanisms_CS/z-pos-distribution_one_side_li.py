import os, sys
import numpy as np 

print ("molecule_name, start_snap, end_snap, deltaT")
print ("eg. WATER/OCTA_OH, 0, 10000, 2")

mole_name = sys.argv[1]

time_b = int(sys.argv[2])  #0
time_e = int(sys.argv[3])  #10000
delta_t = int(sys.argv[4]) #1
t= time_b

amsum = []
while t <= time_e:
    y = []
    x = []
    with open('ion_layer_pdb' + str(t)  + '.pdb') as inputfile:
        print(t)
        lines = inputfile.readlines()
        lengthfile = len(lines)
        inputfile.close()
        for i in range(0,lengthfile,1):
            if str(lines[i].split()[-1]) == 'SYSTLI' :
                x.append(i) 
        print(x)        
        for i in x:
            if (float(lines[i].split()[9]) == 1.00 and str(lines[i].split()[-1]) == 'SYSTLI' ) :
                m = (int((int(lines[i].split()[4][1:]))))
                print(m) 
                amsum.append(float(lines[i].split()[-4]))
            else:
                pass
        #print (y )        
    #with open(mole_name + str(t) + '.gro','r') as inputfile1:
        print(t)
        #print(am)
        #lines1 = inputfile1.readlines()
        #lengthfile1 = len(lines1)
        #inputfile1.close()
        #edge_u = []
        #for i in range(22041,22169,1):
            #if (lines[i].find('# Fix ') != -1):
            #if float(lines1[i].split()[-1]) < 12 :
                #edge_u.append(int(lines1[i].split()[0][:-2]))
        #print("Adjacency matrix: ")
        #printMatrix(adjMatrix) 
        #print (edge_u)
        #for i in range(7282,7411,1):      
            #if i in y: 
                #if i in edge_u: 
                    #for j in range(22041,22169,1):
                        #if (int(lines1[j].split()[0][:-2]) == i) : 
                        #print(i)
                        #cnt = edge_u.count(i)
                            #amsum.append(float(lines1[j].split()[-1]))
            
        

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
np.savetxt('Z-pos_distribution_lithium_layer1_one_side.csv',amsum)
#np.savetxt('wat_wat_hist_bulk.csv',np.column_stack((hist1, bins1)))



