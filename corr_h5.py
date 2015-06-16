import pylab as pl
from modules import functions as f

#read data
filePath = "/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5"

a = f.readFile(filePath)

#accumulate noise
a = f.stackNoise(a)

#scale values

#compute individual  correlations
timeRange = f.getTimeRange(a)

aCorr = f.arrayCorr(a, timeRange)

#compute overall correlation
overall = [aCorr]

overallCorr = f.overallCorr(overall, timeRange)

#plot data
pl.plot(timeRange, overallCorr)
pl.title("Some title")
pl.xlabel("change in time")
pl.ylabel("correlation")
pl.savefig("/mnt/cbis/home/melissa/figures/h5_data.png")
pl.show()
