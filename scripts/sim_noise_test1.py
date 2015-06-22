import numpy as np
import pylab as pl
from modules import new_functions as f
import time
import math

pi = 3.1415926535
#simmulate data
size = (99, 256, 256)

err = [0.1, 0.2, 0.3, 0.4, 0.5]
a_stack_sum = []
for e in err:
    tmp = np.zeros((100, 256, 256))
    tmp[0] = 2*pi*np.random.normal(0, e, (256, 256))-0.5
    tmp[1:] = np.random.normal(0, e, size)
    a_stack_sum.append(np.cos(np.cumsum(tmp, 0)))

#calculate distance
timeRange = f.getTimeRange(a_stack_sum[0])

#plot sum vs time
fig1 = pl.figure(1)
pl.title("Decorrelation Time")
pl.xlabel("frame separation (10ms)")
pl.ylabel("Euclidean distanve between frames")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, dis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/sim_noise__data1.png")
pl.show()

#plot log(sum) vs time
fig2 = pl.figure(2)
pl.title("Decorrelation Time")
pl.xlabel("frame separation (10ms)")
pl.ylabel("log(distance) between frames")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, logDis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/sim_noise_data2.png")
pl.show()

#plot log(sum) vs log(time)
fig3 = pl.figure(3)
pl.title("Decorrelation Time")
pl.xlabel("log(frame separation) (10ms)")
pl.ylabel("log(distance) between frames")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    logTime = [i if i<=0 else math.log(i) for i in timeRange]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(logTime, logDis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/sim_noise_data3.png")
pl.show()
