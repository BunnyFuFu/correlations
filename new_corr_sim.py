import numpy as np
import pylab as pl
from modules import new_functions as f
import time
import math

#simmulate data
size = (100, 256, 256)

err = [0.1, 0.2, 0.3, 0.4, 0.5]
a_stack_sum = []
for e in err:
    tmp = np.random.normal(0, e, size)
    a_stack_sum.append(np.cos(np.cumsum(tmp, 0)))

#calculate distance
timeRange = f.getTimeRange(a_stack_sum[0])

#plot sum vs time
fig1 = pl.figure(1)
pl.title("Decoherence time")
pl.xlabel("time")
pl.ylabel("sum")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, dis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/new_sim_data1.png")
pl.show()

#plot log(sum) vs time
fig2 = pl.figure(2)
pl.title("Decoherence time")
pl.xlabel("time")
pl.ylabel("log(sum)")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, logDis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/new_sim_data2.png")
pl.show()

#plot log(sum) vs log(time)
fig3 = pl.figure(3)
pl.title("Decoherence time")
pl.xlabel("log(time)")
pl.ylabel("log(sum)")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    logDis = [i if i<=0 else math.log(i) for i in dis]
    logTime = [i if i<=0 else math.log(i) for i in timeRange]
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(logTime, logDis, label="SD = %.2f"%e)
pl.legend(loc='lower right')
pl.savefig("/mnt/cbis/home/melissa/figures/simulated/new_sim_data3.png")
pl.show()
