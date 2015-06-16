import numpy as np
import pylab as pl
from modules import new_functions as f
import time
import math

#read data from file
path1 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"
path2 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout2.h5"

files = [path1, path2]
times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_stack_sum = []
for p in files:
    tmp = f.readFile(p)
    a_stack_sum.append(np.cos(np.cumsum(tmp, 0)))

#calculate distance
timeRange = f.getTimeRange(a_stack_sum[0])

#plot sum vs time
fig1 = pl.figure(1)
pl.title("Decoherence time")
pl.xlabel("time")
pl.ylabel("sum")
for p,v in zip(files, a_stack_sum):
    startTime = time.time()
    mean_stack = [f.distanceVaryTime(v, timeRange, t).mean() for t in times]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(range(len(mean_stack)), mean_stack, label="Cutout: %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/vary_time_data1.png")
pl.show()

#plot log(sum) vs time
fig2 = pl.figure(2)
pl.title("Decoherence time")
pl.xlabel("time")
pl.ylabel("log(sum)")
for p,v in zip(files, a_stack_sum):
    startTime = time.time()
    mean_stack = [f.distanceVaryTime(v, timeRange, t).mean() for t in times]
    log_mean_stack = [i if i<=0 else math.log(i) for i in mean_stack]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(range(len(mean_stack)), log_mean_stack, label="Cutout: %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/vary_time_data2.png")
pl.show()

#plot log(sum) vs log(time)
fig3 = pl.figure(3)
pl.title("Decoherence time")
pl.xlabel("log(time)")
pl.ylabel("log(sum)")
for p,v in zip(files, a_stack_sum):
    startTime = time.time()
    mean_stack = [f.distanceVaryTime(v, timeRange, t).mean() for t in times]
    log_mean_stack = [i if i<=0 else math.log(i) for i in mean_stack]
    log_time = [i if i==0 else math.log(i) for i in range(len(mean_stack))]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(log_time, log_mean_stack, label="Cutout: %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/vary_time_data3.png")
pl.show()
