#!/usr/bin/env python3

def maxstring(countB, countA, maxB, maxA):
    count_a = 0
    count_b = 0

    max_a_count = min(countA, maxA)
    max_b_count = min(countB, maxB)

    string = ""

    while countB > 0 or countA > 0:
        if count_a < max_a_count and countA > 0:
            string += "A"
            countA -= 1
            count_a += 1
            count_b = 0
        elif count_b < max_b_count and countB > 0:
            string += "B"
            countB -= 1
            count_b += 1
            count_a = 0
        elif count_a >= max_a_count and countB > 0:
            string += "B"
            countB -= 1
            count_b = 1
            count_a = 0
        elif count_b >= max_b_count and countA > 0:
            string += "A"
            countA -= 1
            count_b = 0
            count_a = 1

if __name__ == "__main__":
    maxstring(5, 3, 1, 1)
