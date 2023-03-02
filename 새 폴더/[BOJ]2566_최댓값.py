arr = [list(map(int, input().split())) for _ in range(9)]
result = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= result:
            result = arr[i][j]
            idx = (i+1, j+1)
print(result)
print(*idx)