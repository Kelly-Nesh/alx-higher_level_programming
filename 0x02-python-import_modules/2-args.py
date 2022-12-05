#!/usr/bin/python3
import sys


def main(*argv):
    cnt = 0
    argc = len(sys.argv) - 1
    if l == 1:
        print("{:d} argument:".format(argc))
    elif l == 0:
        print("{:d} arguments.".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    for arg in sys.argv:
        if (cnt != 0):
            print("{}: {}".format(cnt, arg))
        cnt += 1


if __name__ == "__main__":
    main()
