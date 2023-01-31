T = int(input())

for i in range(T):
    answer = input()
    count = 0
    score = 0
    for j in range(len(answer)):
        result = ''.join(answer)
        if result[j] == 'O':
            count += 1
            score += count
            # print(score)
        else:
            count = 0
    print(score)
