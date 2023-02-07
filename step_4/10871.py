nums, n = map(int,input().split())
lst = list(map(int, input().split()))

result = []

for i in lst:
    if n > i:
        result.append(str(i))

print(' '.join(result))