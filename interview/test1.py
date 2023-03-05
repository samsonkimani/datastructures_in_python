#!/usr/bin/env python3

def maxstring(countB, countA, maxB, maxA):
    string = ""
    i = 1
    if countB > countA:
        string += "B"
        countB -= 1
    else:
        string += "A"
        countA -= 1
    strlen = len(string)
    max_length = countA + countB

    while countB > 0 and countA > 0 and max_length > 0:
        if countB > countA:
            string += "B"
            countB -= 1
        else:
            string += "A" * min (countA
            countA -= 1
    print(string)

if __name__ == "__main__":
    maxstring(5, 3, 1, 1)
