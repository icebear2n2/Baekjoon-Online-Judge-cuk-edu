a, b = map(int, input().split())
m = int(input())

time = (a * 60) + b + m

if time >= 1440:
    time -= 1440
    
print('{} {}'.format((time // 60), (time % 60)))
