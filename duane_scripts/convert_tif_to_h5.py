import re
from PIL import Image
import numpy as np
import glob
import os
import h5py


expTag="08_20150530"
currDir = os.getcwd()
outDir="/mnt/cbis/images/duaneloh/EMData"
newDir = os.path.join(currDir,"../"+expTag)
os.chdir(newDir)
flist = np.array(glob.glob("*.tif"))

s=re.compile("\d+\_\d+\_\d+-(\d+).tif")

def returnTag(txt):
    txx = s.findall(txt)
    return int(txx[0])

ord = np.argsort(np.array([returnTag(ff) for ff in flist]))
sortedFlist=flist[ord]

outputFileName=os.path.join(outDir, expTag+".h5")
fp = h5py.File(outputFileName, "w")

for nn,fn in enumerate(sortedFlist):
    f = np.array(Image.open(fn))
    if nn%100 == 0:
        print nn
    fp.create_dataset("/frames/%05d"%(nn+1), data=f, compression="gzip", compression_opts=9)
    fp.close()
