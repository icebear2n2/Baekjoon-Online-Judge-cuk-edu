n = int(input())
scores = list(map(int, input().split()))
scores.sort()

average = 0

for i in scores:
    average += (i / scores[-1]) * 100

print(average / n)
