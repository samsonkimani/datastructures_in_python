#!/usr/bin/env python3
def maxstring(COUNTA, COUNTB, MAXA, MAXB):
    a_count = 0
    b_count = 0
    output = ""
    while COUNTA > 0 or COUNTB > 0:
        if COUNTA > 0 and a_count < MAXA:
            output += "A"
            COUNTA -= 1
            a_count += 1
            b_count = 0
        elif COUNTB > 0 and b_count < MAXB:
            output += "B"
            COUNTB -= 1
            b_count += 1
            a_count = 0
        elif COUNTA > 0:
            output += "A"
            COUNTA -= 1
            a_count = 1
            b_count = 0
        elif COUNTB > 0:
            output += "B"
            COUNTB -= 1
            b_count = 1
            a_count = 0
    return output

if __name__ == "__main__":
    print(maxstring(5, 3, 1, 1))

