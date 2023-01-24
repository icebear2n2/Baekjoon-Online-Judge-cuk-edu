import sys

n = str(sys.stdin.readline())
lst = [0, 0]
count = 0

if int(n) <= 10:
    n = '0{}'.format(n)

result = n

while True:
    count += 1
    lst[0] = n[1]
    lst[1] = str((int(n[0]) + int(n[1])) % 10)
    n = ''.join(lst)

    if result == n:
        break

print(count)









