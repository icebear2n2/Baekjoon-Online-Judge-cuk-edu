n = list(str(input()).upper())
dic = {}
count = 0
result = ''

for i in set(n):
    dic[i] = n.count(i)

sort_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

if len(n) == 1:
    print(n[0])

for key in sort_dict.keys():
    count += 1

    if count == 1:
        result = key

    elif count > 1:

        if sort_dict[result] == sort_dict[key]:
            print('?')
            break

        else:
            print(result)
            break
