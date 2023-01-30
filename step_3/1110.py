# n >= 10인 경우의 풀이

# n = str(input()) 
# num = n
# lst = list(n)
# count = 0

# while True:
#     count += 1
#     lst[0] = n[1]
#     lst[1] = str((int(n[0]) + int(n[1])) % 10)  

#     n = ''.join(lst) 
#     if n == num:
#         break

# print(count)

n = str(input()) 

if len(n) < 2:
    n = '0{}'.format(n)

num = n
lst = list(n)
count = 0

while True:
    count += 1
    lst[0] = n[1]
    lst[1] = str((int(n[0]) + int(n[1])) % 10)  

    n = ''.join(lst) 
    if n == num:
        break

print(count)