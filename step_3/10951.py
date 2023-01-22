import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if (a + b) == 0:
            break
        else:
            print(a + b)
    except ValueError:
        break