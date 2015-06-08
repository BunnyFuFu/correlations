import numpy as np
from modules import functions as f

#create random data
a = np.random.rand(100, 512, 512)
b = np.random.rand(100, 512, 512)
c = np.random.rand(100, 512, 512)

#TODO:
#Accumulate random stack
#Scale accumulated stack
#Time test summarized in a figure
# - vary array size
# - vary scale

timeRange = f.getTimeRange(a)

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
