import h5py as hp
fp = hp.File("/mnt/cbis/images/duaneloh/EMData/LiquidCutout1.h5", "r")

for i in range(1, 11):
    a = fp[str(i)].value
    print a.sum()
fp.close()

