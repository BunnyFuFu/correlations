import numpy as np
import pylab as pl
from modules import new_functions as F
import time
import math

path1 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"
path2 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout2.h5"

files = [path1, path2]
frameSep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blkSize = [1, 2, 4, 8]
stack_sum = []

#read data from file into 3D array
for p in files:
    tmp = F.readFile(p, size=256)
    stack_sum.append(np.cos(np.cumsum(tmp, 0)))

#plot distance vs frame separation
fig1, ax1 = pl.subplots(1, 2, figsize=(14, 6))
pl.suptitle("Decorrelation Time")

print("256 x 256")
for n,s in enumerate(stack_sum):
    startTime = time.time()
    ax1[n].set_title("Cutout %d"%(n+1))
    for b in blkSize:
        blk_stack = F.avgInStack(s, b)
        avg_stack = [F.measureMeanDistInStack(blk_stack, f) for f in frameSep]
        ax1[n].plot(frameSep, avg_stack, label="Block Size: %d"%(b))
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    pl.xlabel("frame separation (10ms)")
    pl.ylabel("Euclidean distance between frames")
    ax1[n].legend(loc='lower right')

pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/blk_sep_data1.png")
pl.show()

#plot log(distance) vs frame separation
fig2, ax2 = pl.subplots(1, 2, figsize=(14, 6))
pl.suptitle("Decorrelation Time")

print("256 x 256")
for n,s in enumerate(stack_sum):
    startTime = time.time()
    ax2[n].set_title("Cutout %d"%(n+1))
    for b in blkSize:
        blk_stack = F.avgInStack(s, b)
        bRange = range(len(blk_stack))
        avg_stack = [F.measureMeanDistInStack(blk_stack, f) for f in frameSep]
        log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
        ax2[n].plot(frameSep, log_avg_stack, label=" Block Size: %d"%(b))
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    pl.xlabel("frame separation (10ms)")
    pl.ylabel("Euclidean distance between frames")
    ax2[n].legend(loc='lower right')

pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/blk_sep_data2.png")
pl.show()

#plot log(distance) vs log(frame separation)
fig3, ax3 = pl.subplots(1, 2, figsize=(14,6))
pl.title("Decorrelation Time")
pl.xlabel("log(frame separation) (10ms)")
pl.ylabel("log(distance) between frames")

print("256 x 256")
for n,s in enumerate(stack_sum):
    startTime = time.time()
    ax3[n].set_title("Cutout %d"%(n+1))
    for b in blkSize:
        blk_stack = F.avgInStack(s, b)
        bRange = range(len(blk_stack))
        avg_stack = [F.measureMeanDistInStack(blk_stack, f) for f in frameSep]
        log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
        log_time = [i if i==0 else math.log(i) for i in frameSep]
        ax3[n].plot(log_time, log_avg_stack, label="Block Size %d"%(b))
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    pl.xlabel("frame separation (10ms)")
    pl.ylabel("Euclidean distance between frames")
    ax3[n].legend(loc='lower right')

pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/blk_sep_data3.png")
pl.show()
