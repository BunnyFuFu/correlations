import h5py
from mpi4py import MPI
import multiprocessing as mp
import numpy as np
import time
import sys
import cPickle as pickle

fn = "/mnt/cbis/images/duaneloh/EMData/07_20150530.h5"

comm        = MPI.COMM_WORLD
commSize    = comm.Get_size()
rank        = comm.Get_rank()

start_time = MPI.Wtime()
fp = h5py.File(fn, "r")
numFrames = len(fp["frames"].keys())
partition = np.array_split(np.arange(1, numFrames+1), commSize)[rank]
my_powerSpec = None
for f in partition:
    dataField = "frames/%05d"%f
    tmp = fp[dataField].value
    f_tmp = np.abs(np.fft.ifftshift(np.fft.fftn(tmp)))**2
    if my_powerSpec is None:
        my_powerSpec = 1.*f_tmp.copy()
    else:
        my_powerSpec += 1.*f_tmp
fp.close()
all_powerSpec = np.zeros_like(my_powerSpec)
comm.Reduce(my_powerSpec, all_powerSpec, op=MPI.SUM, root=0)

end_time = time.time()
print "Took %lf seconds"%(end_time-start_time)
#Write the result to an h5file


#numProcs = int(sys.argv[1])
#output = mp.Queue(maxsize=numProcs)
#def average_frame(frameNums, output):
#    fp = h5py.File(fn, "r")
#    a = None
#    c = 0
#    for f in frameNums:
#        dataField = "frames/%05d"%f
#        tmp = fp[dataField].value
#        f_tmp = np.abs(np.fft.ifftshift(np.fft.fftn(tmp)))**2
#        c += 1
#        if a is None:
#            a = 1.*f_tmp.copy()
#        else:
#            a += 1.*f_tmp
#    fp.close()
#    print "I'm done with %d frames!"%c
#    curr_tot = 1.*a.sum()
#    output.put(curr_tot)
#
#start_time = time.time()
#partitions = np.array_split(np.arange(1, numFrames+1), numProcs)
#processes = [mp.Process(target=average_frame, args=(nn, output)) for nn in partitions]
#
#for p in processes:
#    p.start()
#
#for p in processes:
#    p.join()
#
#results = [output.get() for p in processes]
#
#tot = 0.
#for r in results:
#    tot += r
#
