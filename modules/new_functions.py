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
    return range(x)

def distance(a, time):
    """calculate distance of each frame from the first frame"""
    sum = [np.sqrt(((a[1] - a[i])**2).flatten().sum()) for i in time]
    sum = np.asarray(sum)
    return sum
