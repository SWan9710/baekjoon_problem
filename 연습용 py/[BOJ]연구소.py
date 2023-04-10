from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y, wall):
    # 종료조건
    if wall == 3:
        BFS(virus)



def BFS(x, y):
    x, y = virus.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if arr[nx][ny] == 0:
                virus.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = deque()
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
            visited[i][j] = 1



# 벽은 무조건 3개
# virus 위치 저장해서 돌기
# visited 배열 만들기
