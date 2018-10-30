# python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = []

    max_el = a[0]
    max_i = 0
    max_c = 0
    for i in range(len(a)):
        if a[i] == max_el:
            max_c += 1

        if a[i] > max_el:
            max_c = 1
            max_el = a[i]
            max_i = i


    if max_c == 1:
        for i in range(len(a)):
            if not i == max_i: 
                result.append(a[i])
    else:
        c = 0
        for i in range(len(a)):
            if a[i] == max_el:
                c += 1

            if not (max_el == a[i] and c == 3): 
                result.append(a[i])

    # print(max_el)
    # print(max_i)
    # print(max_c)
    # your code

    # print('result:')
    print(" ".join(map(str,result)))


if __name__ == '__main__':
    main()