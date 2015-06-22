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
    sum = [np.sqrt(((a[0] - a[i])**2).sum()) for i in range]
    sum = np.asarray(sum)
    return sum

def distanceVaryTime(a, r, timeSep):
    lastVal = r[-1*timeSep]
    sum = [np.sqrt(((a[i] - a[i+timeSep])**2).flatten().mean()) if i<lastVal else 0 for i in r]
    sum = np.asarray(sum[:lastVal])
    return sum

def averageBlock(stack, r, n):
    a = [stack[i:i+n].flatten().mean() for i in np.arange(0, len(r), n)]
    a = np.asarray(a)
    return a
