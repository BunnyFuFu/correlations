import numpy as np
import pylab as pl
from modules import new_functions as f
import time
import math

#read data from file
path1 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"
path2 = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout2.h5"

files = [path1, path2]
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
    dis = f.distance(v, timeRange)
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, dis, label="Liquid Cutout %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/new_data1.png")
pl.show()

#plot log(sum) vs time
fig2 = pl.figure(2)
pl.title("Decoherence time")
pl.xlabel("time")
pl.ylabel("log(sum)")
for p,v in zip(files, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, logDis, label="Liquid Cutout %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/new_data2.png")
pl.show()

#plot log(sum) vs log(time)
fig3 = pl.figure(3)
pl.title("Decoherence time")
pl.xlabel("log(time)")
pl.ylabel("log(sum)")
for p,v in zip(files, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    logTime = [i if i==0 else math.log(i) for i in timeRange]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(logTime, logDis, label="Liquid Cutout %d"%(files.index(p)+1))
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/LiquidCutout/new_data3.png")
pl.show()

