import sys

T = int(sys.stdin.readline())

for i in range(T):
    result = ''
    R, S = map(str, sys.stdin.readline().split())

    for i in S:
        result += (int(R) * i)

    print(result)
