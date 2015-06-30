import struct
import h5py
import sys

in_mrc = "some_file_name.mrc"
out_h5 = "some_file_name.h5"

with open(in_mrc, 'rb') as f:
    all_header_size     = 800
    useful_header_size  = 220
    out_fp = h5py.File(out_h5, "w")
    grp = out_fp.create_group("params")

    # Number of columns, rows, sections (nx,ny,nz,)
    [s, t] = [12, "iii"]
    (nx,ny,nz,) = struct.unpack(t, f.read(s))
    grp.create_dataset("nx", data=nx)
    grp.create_dataset("ny", data=ny)
    grp.create_dataset("nz", data=nz)

    # Pixel type
    # 0 = unsigned or signed bytes
    # 1 = signed short integers (16 bits)
    # 2 = float
    # 3 = short * 2 (used for complex data)
    # 4 = float * 2 (used for complex data)
    # 6 = unsigned 16-bit integers (non-standard)
    # 16 = unsigned char * 3
    [s, t]  = [4, "i"]
    (mode,) = struct.unpack(t, f.read(s))
    grp.create_dataset("mode", data=mode)
    p_typ    = {0:'B', 1:'H', 2:'f', 3:'hh', 4:'ff', 6:'I', 16:'BBB'}
    p_typ_sz = {0:1,   1:2,   2:4,   3:4,    4:8,    6:4,   16:3}

    # Starting point of sub image
    [s, t] = [12, "iii"]
    (nxstart,nystart,nzstart,) = struct.unpack(t, f.read(s))
    grp.create_dataset("nxstart", data=nxstart)
    grp.create_dataset("nystart", data=nystart)
    grp.create_dataset("nzstart", data=nzstart)

    # Grid size in X, Y, Z
    [s, t] = [12, "iii"]
    (mx,my,mz,) = struct.unpack(t, f.read(s))
    grp.create_dataset("mx", data=mx)
    grp.create_dataset("my", data=my)
    grp.create_dataset("mz", data=mz)

    # Cell size; pixel spacing = xlen/mx, ylen/my, zlen/mz
    [s, t] = [12, "fff"]
    (xlen,ylen,zlen,) = struct.unpack(t, f.read(s))
    grp.create_dataset("xlen", data=xlen)
    grp.create_dataset("ylen", data=ylen)
    grp.create_dataset("zlen", data=zlen)
    grp.create_dataset("xcellsize", data=xlen/mx)
    grp.create_dataset("ycellsize", data=ylen/my)
    grp.create_dataset("zcellsize", data=zlen/mz)

    # Cell angles
    [s, t] = [12, "fff"]
    (alpha,beta,gamma,) = struct.unpack(t, f.read(s))
    grp.create_dataset("alpha", data=alpha)
    grp.create_dataset("beta", data=beta)
    grp.create_dataset("gamma", data=gamma)

    # IMOD specific?
    [s, t] = [12, "iii"]
    (mapc,mapr,maps,) = struct.unpack(t, f.read(s))
    grp.create_dataset("mapc", data=mapc)
    grp.create_dataset("mapr", data=mapr)
    grp.create_dataset("maps", data=maps)

    # IMOD scaling?
    [s, t] = [12, "fff"]
    (amin,amax,amean,) = struct.unpack(t, f.read(s))
    grp.create_dataset("amin", data=amin)
    grp.create_dataset("amax", data=amax)
    grp.create_dataset("amean", data=amean)

    # Crystallographic parameters
    # ispg: space group number
    # next: number of bytes in extended header
    [s, t] = [8, "ii"]
    (ispg,next,) = struct.unpack(t, f.read(s))
    grp.create_dataset("ispg", data=ispg)
    grp.create_dataset("next", data=next)

    # ??
    [s, t] = [2, "h"]
    (creatid,) = struct.unpack(t, f.read(s))
    grp.create_dataset("creatid", data=creatid)

    f.seek(128)

    # nint: number of integers per section or bytes per section
    # nreal: Number of reals per section
    [s, t] = [4, "h"]
    (nint,nreal,) = struct.unpack(t, f.read(s))
    grp.create_dataset("nint", data=nint)
    grp.create_dataset("nreal", data=nreal)

    f.seek(152)

    [s, t] = [8, "ii"]
    (imodStamp,imodFlags,) = struct.unpack(t, f.read(s))

    [s, t] = [12, "hhhhhh"]
    (idtype,lens,nd1,nd2,vd1,vd2,) = struct.unpack(t, f.read(s))

    [s, t] = [24, "ffffff"]
    (tilt1,tilt2,tilt3,tilt4,tilt5,tilt6) = struct.unpack(t, f.read(s))

    # Origin of image
    [s, t] = [12, "fff"]
    (xorg,yorg,zorg,) = struct.unpack(t, f.read(s))
    grp.create_dataset("xorg", data=xorg)
    grp.create_dataset("yorg", data=yorg)
    grp.create_dataset("zorg", data=zorg)

    f.seek(all_header_size)

    #There should be nz images, each with size (nx,ny)
    fr_grp      = out_fp.create_group("frames")
    fr_str_txt  = nx*ny*p_typ[mode]
    fr_sz       = nx*ny*p_typ_sz[mode]
    for fnum,frame in enumerate(range(nz)):
        bin_data = f.read(fr_sz)
        fr_data = struct.unpack(fr_sz_txt, bin_data)
        fr_tag  = "%05d"%(fnum+1)
        fr_grp.create_dataset(fr_tag, data=fr_data, compression="gzip", compression_opts=9)

    # All the reading and writing should be done by now
    out_fp.close()
