import pylab as pl
from modules import functions as f

#read data
filePath = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"

a = f.readFile(filePath)

#accumulate noise
a = f.stackNoise(a)

#scale values

#compute correlations
timeRange = f.getTimeRange(a)

aCorr = f.arrayCorr(a, timeRange)

#plot data
pl.plot(timeRage, aCorr)
pl.show()
