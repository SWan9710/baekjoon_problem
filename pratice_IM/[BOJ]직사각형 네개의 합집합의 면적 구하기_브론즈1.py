arr = [[0] * 101 for _ in range(101)]
for tc in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            arr[i][j] += 1

result = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] != 0:
            result += 1
print(result)