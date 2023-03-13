dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS_R(i, j):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                if arr[nx][ny] == 'R':
                    stack.append((nx, ny))
                    arr[nx][ny] = 0

                
def DFS_G(i, j):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                if arr[nx][ny] == 'G':
                    stack.append((nx, ny))
                    arr[nx][ny] = 0


def DFS_B(i, j):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                if arr[nx][ny] == 'B':
                    stack.append((nx, ny))
                    arr[nx][ny] = 0
                    arr2[nx][ny] = 0

                
def DFS_RG(i, j):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr2[nx][ny] != 0:
                    stack.append((nx, ny))
                    arr2[nx][ny] = 0


               
N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = [[''] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr2[i][j] = arr[i][j]

# 적록색약이 아닌사람이 보는 구역의 수
count = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            count += 1
            DFS_R(i, j)
        
        if arr[i][j] == 'G':
            count += 1
            DFS_G(i, j)
            
        if arr[i][j] == 'B':
            count += 1
            count2 += 1
            DFS_B(i, j)

for i in range(N):
    for j in range(N):
        if arr2[i][j] != 0:
            count2 += 1
            DFS_RG(i, j)

print(count, count2)