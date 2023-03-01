n = str(input())
dic = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
count = 0

for key in dic.keys():
    for i in n:
        if i in dic[key]:
            count += (key + 1)

print(count)

