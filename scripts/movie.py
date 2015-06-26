import numpy as np
import pylab as pl
from modules import new_functions as F


path = "/mnt/cbis/images/duaneloh/EMData/19VVG_HM.h5"
stack = F.readFile2(path, size=1024)

pStack = np.array([F.partitionArr(stack[i], w0=128, w1=128) for i in range(321)])

dis = np.array([F.measureDistInStack(pStack[:,i]) for i in range(64)])

fig1 = pl.figure(1, figsize=(6, 10))
fig1.suptitle("Distances Between Frames")
pl.ylabel("frames sorted by time")
pl.xlabel("partitons")
pl.imshow(np.swapaxes(dis, 0, 1))
pl.colorbar()
pl.savefig("/mnt/cbis/home/melissa/figures/distances_128x128.png")
pl.show()

#sort each partition by increasing distances
dCopy = np.copy(dis)
for i in dCopy:
    i.sort()

fig2 = pl.figure(2, figsize=(6, 10))
fig2.suptitle("Distances Between Frames Sorted")
pl.ylabel("frames sorted by ascending distance")
pl.xlabel("partitions")
pl.imshow(np.swapaxes(dCopy, 0, 1))
pl.colorbar()
pl.savefig("/mnt/cbis/home/melissa/figures/dis_sorted_128x128.png")
pl.show()
