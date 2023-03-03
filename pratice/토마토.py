from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque()

count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            x, y = i, j
            queue.append((x, y))
            visited[x][y] = 1
            count += 1

while queue:
    sx, sy = queue.popleft()
    for k in range(4):
        nx, ny = sx + dx[k], sy + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if arr[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1
                count += 1

minus = 0
max_v = 0
for i in range(len(arr)):
    minus += arr[i].count(-1)
    for j in range(M):
        if visited[i][j] > max_v:
            max_v = visited[i][j]

if N*M - count - minus == 0:
    print(max_v-1)
else:
    print(-1)