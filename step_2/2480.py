num_list = list(map(int, input().split()))

dup = [x for i, x in enumerate(num_list) if i != num_list.index(x)]

if len(dup) == 2:
    print(10000 + dup[0] * 1000)
elif len(dup) == 1:
    print(1000 + dup[0] * 100)
else:
    num_list.sort()
    print(num_list[-1] * 100)
