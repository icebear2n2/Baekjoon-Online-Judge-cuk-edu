set1 = set([i for i in range(1, 31)])
set2 = []

for i in range(28):
    set2.append(int(input()))

set2 = set(set2)

lst = list(set1 - set2)
lst.sort()

for i in lst:
    print(i)

