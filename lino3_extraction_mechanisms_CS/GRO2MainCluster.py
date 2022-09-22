import numpy as np
import subprocess
import os
import math
import sys
import networkx as nx
import community


def Main_Cluster_CN(work_dir, init_cn_dir, t, mol_type1, mol_type2, num_mol_1, num_mol_2):

    # initialize cluster dictionaries, list of clusters per time step
    print (num_mol_1)
    print (num_mol_2)
    init_conn_comp_dict = {}
    conn_comp_dict = {}
    # first create "init" adjacency matrix to extract main cluster
    # then create new adjacency matrix from just the main cluster (same mol index)
    # create initial adjacency matrix for this time step
    init_AM = np.zeros((num_mol_1 + num_mol_2,num_mol_1 + num_mol_2))
    # populate adjacency matrix (AM)
    # mols indexed from 0 to (tot num - 1) 
    with open('Combined_WATER_TRIBP4HBonding%s.input.wat%s.xyz.O_TBP%s.xyz.GraphGeod' % ( str(t),str(t), str(t))) as init_graph_file:
    # loop through CN output file and find edges, put into AM
        for line in init_graph_file:
            mol_1 = int(line.split()[0])
            mol_2 = int(line.split()[1])
            if mol_1 >= num_mol_1 and mol_2 >= num_mol_1:
                pass
            else:
                init_AM[mol_1 - 1][mol_2 - 1] = 1
                init_AM[mol_2 - 1][mol_1 - 1] = 1
    # convert adjacency matrix to networkx formation
    init_NX_AM = nx.from_numpy_matrix(init_AM)
    # get the connected component subgraphs as sets in clusters
    init_clusters = []
    init_clusters_gen = nx.connected_components(init_NX_AM)
    
    # write nx clusters to init_clusters list
    for element in init_clusters_gen:
        init_clusters = init_clusters + [list(element)]
    # save init_clusters for this time step
    init_conn_comp_dict['clusters_%s' % t] = init_clusters
    # get main cluster from init_AM
    main_cluster = max(init_conn_comp_dict['clusters_%s' % t],key=len)

    min_size_prot_mol_1 = []
    min_size_prot_mol_2 = []
    
    for mol in main_cluster:
        if mol < num_mol_1:
            min_size_prot_mol_1 += [mol]
    for mol in main_cluster:
        if mol >= num_mol_1:
            min_size_prot_mol_2 += [mol]
    
    return min_size_prot_mol_1, min_size_prot_mol_2



def GRO_MainCluster(work_dir, gro_dir, mol_type, time_step, water_id):

    with open('%s%snoext.gro' % ( mol_type, time_step),'w') as noext_gro:
        # set the extracted water index array to empty
        no_ext_array = []
        # loop through waters in gro for this time step to find ext water
        with open('%s%s.gro' % ( mol_type, time_step)) as gro:
            lines = gro.readlines()
            lengthinfile = len(lines)
            gro.close()
            start = 0 

            noext_gro.write(str(lines[0]))
            noext_gro.write(str(len(water_id)*3) + '\n')
            
            for i in range(0, lengthinfile):
                if (lines[i].find('Generated ') != -1):
                    start = i + 2
            for j in range(start+2, lengthinfile-1):
                # if line is for a water and any atom is outside the range, count it as extracted
                #if (float(lines[j].split()[-4]) < 4.2 or float(lines[j].split()[-4]) > 9.4) and lines[j][5:10] == mol_type:
                if int(lines[j][:5]) in water_id:
                    #no_ext_array = no_ext_array + [lines[j]]
                	#if lines[j][0:5] not in no_ext_array:
                	#	no_ext_array = no_ext_array + [lines[j][0:5]]
                    noext_gro.write(str(lines[j]))
            noext_gro.write(str(lines[lengthinfile-1]))

            ### reopen gro to loop through for writing no_ext gro
            ##with open('%s%s.gro' % (mol_type, time_step)) as gro:
            ##    # open the no_ext gro file to write to
            ##    with open('%s%snoext.gro' % (mol_type, time_step),'w') as noext_gro:
            ##        for line in gro:
            ##            # if the line is for an atom and the molecule index is not in the list of extracted mols, write line
            ##            if len(line) >= 6:
            ##                noext_gro.write(str(int(line.split()[0])-4*len(no_ext_array)) + '\n')
            ##            elif line[0:5] not in no_ext_array:
            ##                noext_gro.write(line)
        
def GRO2OCTA_CONNECT(work_dir, gro_dir, mol_type, time_step, tbp_id):

    with open('%s%sconnect.gro' % (mol_type, time_step),'w') as ext_gro:
        # set the extracted water index array to empty
        no_ext_array = []
        # loop through waters in gro for this time step to find ext water
        with open('%s%s.gro' % (mol_type, time_step)) as gro:
            lines = gro.readlines()
            #print (lines) 
            lengthinfile = len(lines)
            gro.close()
            start = 0 

            ext_gro.write(str(lines[0]))
            ext_gro.write(str(len(tbp_id)*4) + '\n')
            
            for i in range(0, lengthinfile):
                if (lines[i].find('Generated ') != -1):
                    start = i + 2
            for j in range(start+2, lengthinfile-1):
                #print (int(lines[j][:5]))
                #print (tbp_id)
                # if line is for a water and any atom is outside the range, count it as extracted
                #if (float(lines[j].split()[-4]) < 4.2 or float(lines[j].split()[-4]) > 9.4) and lines[j][5:10] == mol_type:
                if int(lines[j][:5]) in tbp_id:
                    #print(a)
                    #pass
                    #no_ext_array = no_ext_array + [lines[j]]
                    #if lines[j][0:5] not in no_ext_array:
                    #   no_ext_array = no_ext_array + [lines[j][0:5]]
                #else:
                    ext_gro.write(str(lines[j]))
            ext_gro.write(str(lines[lengthinfile-1]))



if __name__ == '__main__':

    num_WATER = 6555
    num_TRIBP = 238
    time_b = 1
    time_e = 6660
    delta_t = 1

    #num_time_steps = (time_e - time_b)/delta_t + 1
    residue1_name = 'wat'
    residue2_name = 'O_TBP'
    mol_type1 = 'wat'
    mol_type2 = 'O_TBP' 

    #os.chdir('WATER_GRO_T240_withHexane')
    HB_dir = 'tbp_water'
    gro_dir = 'tbp_water'
    init_cn_dir = 'tbp_water'

    t = time_b

    water_main = []
    tbp_main = []
    while t <= time_e:
        
        WATERid, TRIBPid = Main_Cluster_CN(HB_dir, init_cn_dir, t, mol_type1, mol_type2, num_WATER, num_TRIBP)
        water_main.append((t, len(WATERid)))
        tbp_main.append((t, len(TRIBPid)))
        print(TRIBPid)
        print ('Interfacial Layering Num_TRIBP in Time: %s' % t, len(TRIBPid))

        WATERid = WATERid + np.array(1)
        GRO_MainCluster(HB_dir, gro_dir, mol_type1,t, WATERid)

        TRIBPid = TRIBPid + np.array(1+1775)
        GRO2OCTA_CONNECT(HB_dir, gro_dir, mol_type2, t, TRIBPid)

        t += delta_t
 
