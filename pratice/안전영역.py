import sys
sys.stdin = open('안전.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x,y):
    visited = [[0] * N for _ in range(N)]
    stack = [(x,y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                arr[nx][ny] >= 0
                visited[nx][ny] = 1
                stack.append((nx,ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    while True:
        count = N*N+1
        # print(count)

        for i in range(N):
            for j in range(N):
                # 비가 1만큼 왔을때
                if arr[i][j] == 0:
                    continue
                arr[i][j] -= 1

        for i in range(N):
            for j in range(N):
                if arr[i][j] >= 0:
                    count -= 1
                    x, y = i, j
                    DFS(x, y)
        print(f'#{tc}',count)
        stop = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    stop += 1

        if stop == N*N:
            break
