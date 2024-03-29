
def dfs(n, lst):
    # 종료조건
    if n == M:
        result.append(lst)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst+[i])
            visited[i] = 0

N, M = map(int, input().split())
result = []
visited = [0] * (N+1)

dfs(0, [])
for lst in result:
    print(*lst)