import numpy as np
from numpy import linalg as LA
from matplotlib import pyplot as P
import h5py as hp

def readFile(path, size=256):
    fp = hp.File(path, 'r')
    a = [fp[str(i)].value for i in range(1, 201)]
    a = np.asarray(a)
    a = a[:, 0:size, 0:size]
    return a

def measureDist(a, b):
    sz = 1.*np.sqrt(a.shape[0]*a.shape[1])
    return LA.norm(a-b)/sz

def measureDistInStack(s, sep=1):
    l = len(s)
    rng = range(l)
    zS = zip(rng[:l-sep], rng[sep:])
    return np.array([measureDist(s[s0],s[s1]) for s0,s1 in zS])

def measureMeanDistInStack(s, sep=1):
    return np.mean(measureDistInStack(s, sep=sep))

def simulatePhasorStack(sd, sz=(100,256,256)):
    arr = np.random.normal(0., sd, size=sz)
    arr[0] += 2.*np.pi*(np.random.rand(*(sz[1:]))-0.5)
    arr = np.cumsum(arr, axis=0)
    return np.cos(arr)

def partitionArr(arr, w0=None, w1=None):
    sh = arr.shape
    if w0 is None:
        w0 = int(np.ceil(sh[0]/10.))
    if w1 is None:
        w1 = int(np.ceil(sh[1]/10.))
    v = []
    row_zip_range = zip(range(0,sh[0],w0), range(w0,sh[0],w0)+[sh[0]])
    col_zip_range = zip(range(0,sh[1],w1), range(w1,sh[1],w1)+[sh[1]])
    for r0,r1 in row_zip_range:
        for c0,c1 in col_zip_range:
            v.append(arr[r0:r1, c0:c1])
    return v

def avgInStack(s, b):
    l = len(s)
    l_zip_range = zip(range(0,l,b), range(b,l,b))
    return np.array([s[l0:l1].mean(axis=0) for l0,l1 in l_zip_range])

"""def simulateAndPlotDefaultCase(avg=0):
    dist_vs_std = []
    std_range = np.arange(0.2, 1., 0.2)
    P.figure()
    P.title("Mean distance vs stdDev (%d-frame average)"%avg)
    for s in std_range:
        stack = simulatePhasorStack(s)
        if avg > 0:
            stack = avgInStack(stack, avg)
        d = [measureMeanDistInStack(stack, sep=ss) for ss in range(30)]
        P.plot(d, label="std=%0.2f"%s)
        dist_vs_std.append(d)
    P.legend(fontsize=9, loc='lower right')
    P.show()"""
