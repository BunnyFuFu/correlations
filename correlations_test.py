import numpy as np
from correlations import functions as f

#create random data
a = np.random.rand(100, 512, 512)
b = np.random.rand(100, 512, 512)
c = np.random.rand(100, 512, 512)

timeRange = getTimeRange(a)

#calculate indiviual correlations
aCorr = f.arrayCorr(a, timeRange)
bCorr = f.arrayCorr(b, timeRange)
cCorr = f.arrayCorr(c, timeRange)

#combine data
overall = [aCorr, bCorr, cCorr]

#calculate overall correlation
overallCorr = f.overallCorr(overall, timeRange)

#generate figure
f.generateOverallGraph(overallCorr)