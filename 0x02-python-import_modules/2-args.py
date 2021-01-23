#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    len_argv = len(argv) - 1

    if len_argv == 0:
        print("{} arguments.".format(len_argv))

    elif len_argv == 1:
        print("{} argument:".format(len_argv))
        for idx in range(len_argv):
            print("{}: {}".format(idx + 1, argv[idx + 1]))

    else:
        print("{} arguments:".format(len_argv))
        for idx in range(len_argv):
            print("{}: {}".format(idx + 1, argv[idx + 1]))
