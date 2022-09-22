import MDAnalysis as mda
import pytim
#from   pytim.datafiles import ILBENZENE_GRO

u = mda.Universe('tbp_wat_hex_lino_5m_nvt_40ns.gro')
# LIG is benzene
g = u.select_atoms('resname SOL or resname LI or resname NITRA')
# 1. To switch from the simple clustering scheme to DBSCAN, set the `cluster_threshold_density`
# 2. To estimate correctly the local density, use a larger cutoff than that of the simple clustering
# 3. With `cluster_threshold_density='auto'`, the threshold density is estimated by pytim
inter  = pytim.ITIM(u,group=g,cluster_cut=10.,cluster_threshold_density='auto',alpha=1.5)
inter.writepdb('layers_test.pdb',centered='middle')




