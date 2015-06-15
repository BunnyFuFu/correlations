import numpy as np
import pylab as pl
from modules import new_functions as f
import time

#time script runtime
startTime = time.time()

#simmulate data
size = (100, 256, 256)
a = np.random.normal(0, 0.01, size)
b = np.random.normal(0, 0.02, size)
c = np.random.normal(0, 0.05, size)

#cumulative sum
aSum = np.cumsum(a, 0)
bSum = np.cumsum(b, 0)
cSum = np.cumsum(c, 0)

cosA = np.cos(aSum)
cosB = np.cos(bSum)
cosC = np.cos(cSum)

#calculate distance
timeRange = f.getTimeRange(cosA)

aDis = f.distance(cosA, timeRange)
bDis = f.distance(cosB, timeRange)
cDis = f.distance(cosC, timeRange)

#plot results
pl.plot(timeRange, aDis, label="SD = 0.01")
pl.plot(timeRange, bDis, label="SD = 0.02")
pl.plot(timeRange, cDis, label="SD = 0.05")
pl.title("Decoherence time(?)")
pl.xlabel("time")
pl.ylabel("sum")
pl.legend(loc='upper right')
endTime = time.time() - startTime
pl.show()
