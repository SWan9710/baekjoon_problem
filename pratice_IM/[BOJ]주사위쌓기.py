# 첫줄 주사위 갯수 입력됨
N = int(input())
dice = []
for i in range(N):
    dice.append(list(map(int, input().split())))

for i in dice:
    print(i)
    for idx, j in enumerate(i):
        if j == 6:
            print(i[0],i[5])