n = int(input())
score = map(int, input().split())

result = 0
new_score = []
for i in score:
    new_score.append(i)
    result += i
new_score.sort()
print((result / new_score[-1] * 100)/len(new_score))


    