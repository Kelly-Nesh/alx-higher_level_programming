#!/usr/bin/python3
from sys import argv
def main():
    argc = len(argv)-1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:\n{}: {}".format(argc, argc, argv[argc]))
    else:
        print("{} arguments:".format(argc))
        for arg in range(1, argc+1):
            print("{}: {}".format(arg, argv[arg]))
if __name__ == "__main__":
    main()
