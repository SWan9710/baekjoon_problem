N, M = map(int, input().split())
arr = [0] * (N+1)
for i in range(1,N+1):
    arr[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*arr[1:])
