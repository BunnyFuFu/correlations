import numpy as np
import pylab as pl
from modules import new_functions as F
import time
import math

path1 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"
path2 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout2.h5"

files = [path1, path2]
frameSep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stack_sum_256 = []
stack_sum_128 = []

#read data from file into 3D array
for p in files:
    tmp = F.readFile(p, size=256)
    stack_sum_256.append(np.cos(np.cumsum(tmp, 0)))

for p in files:
    tmp = F.readFile(p, size=128)
    stack_sum_128.append(np.cos(np.cumsum(tmp, 0)))

#plot distance vs frame separation
fig1, (f1, f2) = pl.subplots(1, 2, figsize=(14,6))
pl.suptitle("Decorrelation Time")

print("256 x 256")
for p,s in zip(files, stack_sum_256):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    f1.set_xlabel("frame separation (10ms)")
    f1.set_ylabel("Euclidean distance between frames")
    f1.plot(frameSep, avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f1.legend(loc='lower right')

print("128 x 128")
for p,s in zip(files, stack_sum_128):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    f2.set_xlabel("frame separation (10ms)")
    f2.set_ylabel("Euclidean distance between frames")
    f2.plot(frameSep, avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f2.legend(loc='lower right')

pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/frame_sep_data1.png")
pl.show()

#plot log(distance) vs frame separation
fig2, (f1, f2) = pl.subplots(1, 2, figsize=(14, 6))
pl.suptitle("Decorrelation Time")

print("256 x 256")
for p,s in zip(files, stack_sum_256):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    f1.set_xlabel("frame separation (10ms)")
    f1.set_ylabel("log(distance) between frames")
    f1.plot(frameSep, log_avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f1.legend(loc='lower right')

print("128 x 128")
for p,s in zip(files, stack_sum_128):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    f2.set_xlabel("frame separation (10ms)")
    f2.set_ylabel("log(distance) between frames")
    f2.plot(frameSep, log_avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f2.legend(loc='lower right')

pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/frame_sep_data2.png")
pl.show()

#plot log(distance) vs log(frame separation)
fig3, (f1, f2) = pl.subplots(1, 2, figsize=(14,6))
pl.suptitle("Decorrelation Time")

print("256 x 256")
for p,v in zip(files, stack_sum_256):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
    log_time = [i if i==0 else math.log(i) for i in frameSep]
    endTime = time.time()
    print("Took %lf seconds" %(endTime  - startTime))
    f1.set_ylabel("log(frame separation) (10ms)")
    f1.set_ylabel("log(distance) between frames")
    f1.plot(log_time, log_avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f1.legend(loc='lower right')

print("128 x 128")
for p,v in zip(files, stack_sum_128):
    startTime = time.time()
    avg_stack = [F.measureMeanDistInStack(s, f) for f in frameSep]
    log_avg_stack = [i if i<=0 else math.log(i) for i in avg_stack]
    log_time = [i if i==0 else math.log(i) for i in frameSep]
    endTime = time.time()
    print("Took %lf seconds" %(endTime - startTime))
    f2.set_xlabel("log(frame separation) (10ms)")
    f2.set_ylabel("log(distance) between frames")
    f2.plot(log_time, log_avg_stack, label="Cutout: %d"%(files.index(p)+1))
    f2.legend(loc='lower right')

pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/frame_sep_data3.png")
pl.show()
