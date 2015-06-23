import numpy as np
import pylab as pl
import h5py as hp

def readFile(filePath):
    fp = hp.File(filePath, "r")
    x, y = fp["1"].shape
    a = [fp[str(i)].value for i in range(1, 10001)]
    a = np.asarray(a)
    return a

def getTimeRange(a):
    x, y, z = a.shape
    return range(x-1)

def stackNoise(a, noise=None):
    x, y, z = a.shape
    if noise is None:
        noise = np.random.rand(y, z)

    total = a[0]
    for i in range(1,x):
        a[i] = total + noise
        total = total + a[i]
    return a

def scaleStack(a, factor=1):
    scaled = a * factor
    return scaled

def arrayCorr(a, time):
    """returns list of correlations given a 3D array"""
    corr = [(np.abs(a[i] - a[i+1])**2).flatten().mean() for i in time]
    return corr

def overallCorr(data, time):
    """returns list of  correlations of entire sample"""
    dataArray = np.asarray(data)
    corr = [dataArray[:,i].mean() for i in time]
    return corr

def generateIndivGraph(a):
    """plots correlation vs change in time
    given one 3D array
    """
    timeRange = range(len(a))
    pl.plot(timeRange, arrayCorr(a, timeRange))
    pl.title("Some title?")
    pl.xlabel("change in time")
    pl.ylabel("correlation")
    pl.show()

#def generateOverallGraph(*args):
#    """Plots correlation vs change in time"""
#
#    timeRange = range(len(args[0]))
#    for a in args:
#        pl.plot(timeRange, a)
#    pl.title("Some title?")
#    pl.xlabel("change in time")
#    pl.ylabel("correlation")
#    pl.legend(loc='upper right')
#    pl.show()

