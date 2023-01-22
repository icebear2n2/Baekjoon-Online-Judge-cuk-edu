import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    print((' ' * (i-1)) + ('*' * ((n+1) -i)))
