n = int(input())

for i in range(n):
    lines = str(input())
    count = 0
    score = 0

    for i in lines:
        if i == 'X':
            count = 0
        
        else:
            count += 1
            score += count
            
    print(score)