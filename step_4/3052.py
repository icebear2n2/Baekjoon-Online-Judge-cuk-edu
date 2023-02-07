lst = []

for i in range(10):
    lst.append(int(input()) % 42)

lst = list(set(lst))

print(len(lst))