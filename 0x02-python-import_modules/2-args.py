#!/usr/bin/python3

import sys

argc = len(sys.argv) - 1

if argc == 0:
    print("0 arguments.")

else:
    print(argc, "arguments" + ("s" if argc > 1 else "") + ":")
    for i in range(1, argc + 1):
	    print(i, ":", sys.argv[i])
