S = list(str(input()))
lst = []

for i in range(97, 123):
    if chr(i) not in S:
        lst.append('-1')
    else:
        lst.append(str(S.index(chr(i))))

print(' '.join(lst))

