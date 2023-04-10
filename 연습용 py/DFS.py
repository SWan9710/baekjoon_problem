'''
입력
7 8
1 2 
1 3 
2 4 
2 5 
4 6 
5 6 
6 7 
3 7
출력 결과
1 2 4 6 5 7 3
1 3 7 6 5 2 4
'''
def DFS(i, k):  # 중복없이 빠짐없이 방문할거
    # 1. 방문체크
    visited[i] = 1
    # 현재의 노드번호 출력
    print(i, end=' ')

    # 현재 노드와 인접하고 방문한적이 없는경우
    for j in graph[i]:
        if visited[j] == 0:
            DFS(j, k)
    


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]


for _ in range(E):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (V+1)
DFS(1, E)