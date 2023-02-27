N, M = map(int, input().split())
# N 바구니 갯수, M 공을 넣는 횟수
arr = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())

    for ball in range(i-1,j):
        arr[ball] = k

print(*arr)
