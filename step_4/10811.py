n, m = map(int, input().split())
dic = {}
save = 0

for i in range(1, n+1):
    dic[i] = i

for i in range(m):
    ball_1, ball_2 = map(int, input().split())
    balls = [ i for i in range(ball_1, ball_2+1)]

    if len(balls) <= 2:
        save = dic[ball_1]
        dic[ball_1] = dic[ball_2]
        dic[ball_2] = save

        print(dic)
    else:
        pass
