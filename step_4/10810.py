n, m = map(int, input().split())
basket = ['0'] * n

for i in range(m):
    balls = list(map(str, input().split()))

    for j in range(int(balls[0]), int(balls[1]) + 1):
        basket[j-1] = balls[2]
    

print(' '.join(basket))