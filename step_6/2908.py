a, b = map(str, input().split())
rev = []

rev.append(int("".join(reversed(a))))
rev.append(int("".join(reversed(b))))

rev.sort()

print(rev[-1])