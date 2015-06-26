import numpy as np
import pylab as pl
from modules import new_functions as F


path = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"
stack = F.readFile(path, size=256)

pStack = np.array([F.partitionArr(stack[i], w0=32, w1=32) for i in range(10000)])

dis = np.array([F.measureDistInStack(pStack[:,i]) for i in range(64)])

fig1 = pl.figure(1, figsize=(6, 10))
fig1.suptitle("Distances Between Frames (Cutout 1)")
pl.ylabel("frames sorted by time")
pl.xlabel("partitions")
pl.imshow(np.swapaxes(dis, 0, 1), aspect='auto')
pl.colorbar()
pl.savefig("/mnt/cbis/home/melissa/figures/liq1_dis.png")
pl.show()

#sort each partition by increasing distances
dCopy = np.copy(dis)
for i in dCopy:
    i.sort()

fig2 = pl.figure(2, figsize=(6, 10))
fig2.suptitle("Distances Between Frames Sorted (Cutout 1)")
pl.ylabel("frames sorted by ascending distance")
pl.xlabel("partitions")
pl.imshow(np.swapaxes(dCopy, 0, 1), aspect='auto')
pl.colorbar()
pl.savefig("/mnt/cbis/home/melissa/figures/liq1_dis_sorted.png")
pl.show()
