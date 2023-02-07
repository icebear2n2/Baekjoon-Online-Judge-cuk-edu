c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    student = scores.pop(0)

    average_score = sum(scores) / student
    high_student = 0

    for i in scores:
        if i > average_score:
            high_student += 1

    print('{:.3f}%'.format((high_student * 100) / student))

