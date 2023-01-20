num1 = int(input())
num2 = "".join(reversed(str(input())))
result = 0

for i in num2:
    print(num1 * int(i)) 

print(num1 * int("".join(reversed(num2))))

