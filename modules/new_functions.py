import numpy as np
import h5py as hp

def readFile(filePath, size=256):
    fp = hp.File(filePath, "r")
    a = [fp[str(i)].value for i in range(1, 201)]
    a = np.asarray(a)
    a = a[:, 0:size, 0:size]
    return a

def getTimeRange(a):
    x, y, z = a.shape
    return range(x)

def distance(a, range):
    """calculate distance of each frame from the first frame"""
    sum = [np.sqrt(((a[0] - a[i])**2).flatten().sum()) for i in range]
    sum = np.asarray(sum)
    return sum

def distanceVaryTime(a, r, time):
    lastVal = r[-1*time]
    sum = [np.sqrt(((a[i] - a[i+time])**2).flatten().sum()) if i<lastVal else 0 for i in r]
    sum = np.asarray(sum[:lastVal])
    return sum

