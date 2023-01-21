x = int(input())
y = int(input())

if x >= 1 and y >= 1:
    print(1)
elif x < 0 and y >= 1:
    print(2)
elif x >=1 and y < 0:
    print(4)
else:
    print(3)

