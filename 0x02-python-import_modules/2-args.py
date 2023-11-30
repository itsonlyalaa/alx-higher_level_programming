#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argstr = "{:d} argument"
argcs = len(sys.argv) - 1
if argcs == 0:
    argstr += 's.'
elif argcs == 1:
    argstr += ':'
else:
    argstr += 's:'
print(argstr.format(argcs))

x = 0
for arg in sys.argv:
    if x != 0:
        print("{:d}: {:s}".format(x, arg))
    x += 1
