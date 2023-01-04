#!/usr/bin/python3
import sys
argc = len(sys.argv)-1
if argc != 1:
    print("Usage: nqueens N")
    sys.exit(1)
if not isinstance(argv[1], (int)):
    print("N must be a number")
    sys.exit(1)
if argv[4] < 4:
    print("N must be at least 4")
    sys.exit(1)
