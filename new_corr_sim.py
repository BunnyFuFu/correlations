import numpy as np
import pylab as pl
from modules import new_functions as f
import time

#time script runtime

#simmulate data
size = (100, 256, 256)

err = [0.1, 0.2, 0.3]
a_stack_sum = []
for e in err:
    tmp = np.random.normal(0, e, size)
    a_stack_sum.append(np.cos(np.cumsum(tmp, 0)))

#calculate distance
timeRange = f.getTimeRange(a_stack_sum[0])

fig = pl.figure()
pl.title("Decoherence time(?)")
pl.xlabel("time")
pl.ylabel("sum")
for e,v in zip(err, a_stack_sum):
    startTime = time.time()
    dis = f.distance(v, timeRange)
    endTime = time.time()
    print("Took %lf seconds" % (endTime - startTime))
    pl.plot(timeRange, dis, label="SD = %lf"%e)
pl.legend(loc='upper right')
pl.show()
