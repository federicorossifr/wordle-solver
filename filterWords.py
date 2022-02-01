from ctypes import sizeof
import sys

fname = sys.argv[1];
fname_filter = fname + ".wslv"
with open(fname) as f:
    with open(fname_filter,"w") as ff:
        for line in f:
            sline = line.rstrip()
            if(len(sline) == 5):
                ff.write(sline.lower())
                ff.write("\n")

