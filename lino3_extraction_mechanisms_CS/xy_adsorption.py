import os
import shutil
import stat
import fileinput
import numpy as np

time_b = 1
time_e = 5000
delta_t = 1

x_value = []
y_value = []
# set intital time and loop through time steps
t = time_b
while t <= time_e:
	print(t)
	TBP_xyz = open('O_TBP%sconnect_correct.gro' % t)
	TBP_xyz_lines = TBP_xyz.readlines()
	lengthfile = int(len(TBP_xyz_lines))
	for tbp in range(2,lengthfile-1,4):
		#if water in y:
		TBP_xpos = 10*float(TBP_xyz_lines[tbp].split()[-3])
		TBP_ypos = 10*float(TBP_xyz_lines[tbp].split()[-2])
		TBP_zpos = 10*float(TBP_xyz_lines[tbp].split()[-1])
		print(TBP_xpos)
		x_value.append(TBP_xpos)
		y_value.append(TBP_zpos)
		TBP_xyz.close()	
	t += delta_t
np.savetxt('xz_distance_adsorbed_tbp.csv',np.column_stack((x_value,y_value)))

