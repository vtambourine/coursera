# python3

import sys

def main():
    n = input()
    c = 0
    all9 = True

    for char in n:
        c += 1
        
        if all9 and char != '9': 
            all9 = False 

    print(c + 1) if all9 else print(c)


if __name__ == '__main__':
    main()