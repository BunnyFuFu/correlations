import numpy as np
import pylab as pl
from modules import functions as f
import time

#time script runtime
startTime = time.time()

#create random data
a = np.random.rand(100, 256, 256)
b = np.random.rand(100, 256, 256)
c = np.random.rand(100, 256, 256)

#Accumulate random stack
a = f.stackNoise(a)
b = f.stackNoise(b)
c = f.stackNoise(c)

#Scale accumulated stack
factor1 = 1
a1 = f.scaleStack(a, factor1)
b1 = f.scaleStack(b, factor1)
c1 = f.scaleStack(c, factor1)

factor2 = 2
a2 = f.scaleStack(a, factor2)
b2 = f.scaleStack(b, factor2)
c2 = f.scaleStack(c, factor2)

factor3 = 3
a3 = f.scaleStack(a, factor3)
b3 = f.scaleStack(b, factor3)
c3 = f.scaleStack(c, factor3)

#Time test summarized in a figure
# - vary array size
# - vary scale

timeRange = f.getTimeRange(a)

#calculate indiviual correlations
aCorr1 = f.arrayCorr(a1, timeRange)
bCorr1 = f.arrayCorr(b1, timeRange)
cCorr1 = f.arrayCorr(c1, timeRange)

aCorr2 = f.arrayCorr(a2, timeRange)
bCorr2 = f.arrayCorr(b2, timeRange)
cCorr2 = f.arrayCorr(c2, timeRange)

aCorr3 = f.arrayCorr(a3, timeRange)
bCorr3 = f.arrayCorr(b3, timeRange)
cCorr3 = f.arrayCorr(c3, timeRange)

#combine data
overall1 = [aCorr1, bCorr1, cCorr1]
overall2 = [aCorr2, bCorr2, cCorr2]
overall3 = [aCorr3, bCorr3, cCorr3]

#calculate overall correlation
overallCorr1 = f.overallCorr(overall1, timeRange)
overallCorr2 = f.overallCorr(overall2, timeRange)
overallCorr3 = f.overallCorr(overall3, timeRange)

#generate figure
#f.generateOverallGraph(overallCorr1, overallCorr2, overallCorr3)
pl.plot(timeRange, overallCorr1, label="x1.0")
pl.plot(timeRange, overallCorr2, label="x2.0")
pl.plot(timeRange, overallCorr3, label="x3.0")
pl.title("Some title?")
pl.xlabel("change in time")
pl.ylabel("correlation")
pl.legend(loc='upper right')
endTime = time.time() - startTime
pl.figtext(1, 1, "{:.3f} seconds".format(endTime))
pl.show()
