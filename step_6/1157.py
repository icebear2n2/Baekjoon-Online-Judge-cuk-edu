n = list(str(input()).upper())
dic = {}

for i in set(n):
    dic[i] = n.count(i)

sort_dict = dict(sorted(dic.items(), key=lambda x: x[1]))

