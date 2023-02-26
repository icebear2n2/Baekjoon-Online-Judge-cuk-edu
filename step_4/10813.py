n, m = map(int, input().split())
dic = {}
result = ''
save = 0

for i in range(1, n+1):
    dic[i] = i

for i in range(m):
    balls = list(map(int, input().split()))

    if balls[0] in dic:
        save = dic[balls[0]]
        dic[balls[0]] = dic[balls[1]]
        dic[balls[1]] = save
    elif balls[1] in dic:
        save = dic[balls[1]]
        dic[balls[1]] = dic[balls[0]]
        dic[balls[0]] = save

for val in dic.values():
    result += str(val)

print(' '.join(result))

