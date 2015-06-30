import h5py
from mpi4py import MPI
import multiprocessing as mp
import numpy as np
import time
import sys
import cPickle as pickle

# To run this script use:
# mpiexec -n <numProcesses> python mpifft.py <input arguments>

fn      = "/mnt/cbis/images/duaneloh/EMData/07_20150530.h5"
out_fn  = "out.h5"
# Uncomment the line below to use the command line to specify file
#fn = sys.argv[1]
#out_fn = sys.argv[2]

comm        = MPI.COMM_WORLD
commSize    = comm.Get_size()
rank        = comm.Get_rank()

start_time = MPI.Wtime()

fp = h5py.File(fn, "r")
numFrames = len(fp["frames"].keys())
partition = np.array_split(np.arange(1, numFrames+1), commSize)[rank]
my_powerSpec = None

for c,f in enumerate(partition):
    dataField = "frames/%05d"%f
    tmp = fp[dataField].value
    f_tmp = np.abs(np.fft.ifftshift(np.fft.fftn(tmp)))**2
    #TODO: Apply blurred Gaussian mask
    if my_powerSpec is None:
        my_powerSpec = 1.*f_tmp.copy()
    else:
        my_powerSpec += 1.*f_tmp
    if c%50 == 0:
        print "Rank:%d done with %d"%(rank, c+1)
fp.close()

all_power_spectrum = np.zeros_like(my_powerSpec)
comm.Reduce(my_powerSpec, all_power_spectrum, op=MPI.SUM, root=0)

end_time = MPI.Wtime()
print "Took %lf seconds"%(end_time-start_time)

#Write the result to an h5file
#TODO: Compute angular average, and save to file
if rank == 0:
    print "Rank %d writing power spectrum to %s"%(rank, out_fn)
    fp = h5py.File(out_fn, "w")
    fp.create_dataset("power_spectrum", data=all_power_spectrum, compression="gzip", compression_opts=9)
    fp.close()
