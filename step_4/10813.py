n, m = map(int, input().split())
dic = {}
save = 0
save2 = 0
for i in range(1, n+1):
    dic[i] = i

for i in range(m):
    balls = list(map(int, input().split()))
    save = dic[balls[0]]
    save2 = dic[balls[1]]

    dic[balls[0]] = save2
    dic[balls[1]] = save

print(*dic.values())
