n = list(str(input()).upper())
count = []

for i in set(n):
    if n.count(i) > 1:
        count.append(i)

if len(n) == 1:
    print(n[0])

elif len(n) == len(set(n)) or len(count) > 1:
    print('?')

else:
    print(count[0])
