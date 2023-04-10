dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 바이러스 놓을수 있는 위치
        if arr[i][j] == 2:
            virus.append((i,j))
            visited[i][j] = 1

while virus:
    sx, sy = virus.pop(0)
    for k in range(4):
        nx, ny = sx + dx[k], sy + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 바이러스가 들어갈 수 있는 공간
            if arr[nx][ny] == 0:
                virus.append((nx, ny))
                # 누적합
                visited[nx][ny] = visited[sx][sy] + 1

for lst in visited:
    print(lst)


# tq