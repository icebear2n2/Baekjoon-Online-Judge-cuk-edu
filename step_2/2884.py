h, m = map(int, input().split())
time = (h * 60) + m

if time < 45:
    time += 1440

result = time - 45

print('{} {}'.format((result // 60), (result % 60)))