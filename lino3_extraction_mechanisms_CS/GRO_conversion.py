import os, sys

print ("molecule_name, start_snap, end_snap, deltaT")
print ("eg. WATER/OCTA_OH, 0, 10000, 2")

mole_name = sys.argv[1]

time_b = int(sys.argv[2])  #0
time_e = int(sys.argv[3])  #10000
delta_t = int(sys.argv[4]) #1

t= time_b

while t <= time_e:
    with open('wat%snoext_connect_correct.gro' % (t),'w') as gro1:
        with open('wat%snoext.gro' % (t)) as gro:

            lines = gro.readlines()
            lengthinfile = len(lines)
            a = lengthinfile-3
            gro.close()
            start = 0 
            for i in range(0, lengthinfile):
                if (lines[i].find('Generated') != -1):
                    start = i + 2
            for j in range(0, lengthinfile):
                if j == 0 :
                    gro1.write(lines[0])
                elif j == 1 : 
                    gro1.write(str(a)+'\n') 
                elif i>1 :    

                # if line is for a water and any atom is outside the range, count it as extracted
                #if (float(lines[j].split()[-4]) < 4.2 or float(lines[j].split()[-4]) > 9.4) and lines[j][5:10] == mol_type:
                #if int(lines[j][:5]) in tbp_id:
                    #pass
                    #no_ext_array = no_ext_array + [lines[j]]
                    #if lines[j][0:5] not in no_ext_array:
                    #   no_ext_array = no_ext_array + [lines[j][0:5]]
                #else:
                    gro1.write(str(lines[j]))
                else :
                    pass    
            #gro1.write(str(lines[lengthinfile-1]))
    t += delta_t
