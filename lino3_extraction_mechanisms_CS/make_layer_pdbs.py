import subprocess
import os
import math
import MDAnalysis as mda
import numpy as np
import pytim
import sys

def main():

	# set variables for anlaysis
	num_WATER = 7205
	time_b = int(sys.argv[1])
	time_e = int(sys.argv[1]) 
	delta_t = 1
	num_time_steps = (time_e - time_b)/delta_t + 1
	mol_type = 'SOL'
	num_layers = 5

	#os.chdir('layer_analysis')

	# loop through time steps to make layers
	time_step = time_b
	while time_step <= time_e:
		print(time_step)
		# read in gro file into MDAnalysis
		u=mda.Universe('wat%snoext_connect_correct.gro' % str(time_step))
		# calculate interfaces
		interface = pytim.ITIM(u,mesh=0.2,alpha=1.5,max_layers=num_layers,radii_dict={'O':1.5,'H':0.0,'M':0.0, 'NA':1.2196})
		# loop through interfaces and write to pdb files
		for layer in range(1):
			interface.writepdb('water_layer_pdbs%s.pdb' % (str(time_step)),centered='middle')#group=interface.atoms.in_layers[:,layer])
		time_step += delta_t


if __name__ == '__main__':
  main()


