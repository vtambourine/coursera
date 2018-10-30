# python3
# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1

    # your code
    # in a infinite loop
    # calculate next element of the sequence
    # i := sequence item
    # if A_i == z return i. break
    # if A_i - y > z return -1
    # print(x, y, z)

    direction = 0 if (x == y) else int((x - y) / abs(x - y))

    # out = "0 "

    a_0 = 0
    a_1 = a_2 = 0
    i = 0

    if z == 0:
        print(0)
        return

    while True:
        i += 1
        a_1 = a_2 + x
        # out += f"{a_1} "
        if a_1 == z:
            result = i
            break

        if direction == -1:
            if a_1 < z:
                result = -1
                break


        i += 1
        a_2 = a_1 - y
        # out += f"{a_2} "
        if a_2 == z:
            result = i
            break

        if direction == 1:
            if a_2 > z:
                result = -1
                break

        if direction == 0:
            result = -1
            break


        if i > 1e4:
            break

    # print(out)

    # print("result:")
    print(result)

if __name__ == '__main__':
    main()