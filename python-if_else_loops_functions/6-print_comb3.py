#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if (i < k):
            print("{:d}{:d}".format(i, k), end="")
            if i < 8:
                print(", ", end="")
print("")
