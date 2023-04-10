# # 최소비용 구하기

# def dijkstra(now):
#     # 방문표기
#     visited = [0] * (N+1)
#     visited[now] = 1

#     # 인접 행렬 정보 기반, 첫 시작 지점에서 각 노드별 방문 가능 거리 기록
#     for next in range(N+1):
#         distance[next] = graph[now][next]
    
#     for _ in range(N):
#         # 가중치와 최솟값 초기화
#         w = 0
#         minV = 10000

#         for i in range(N+1):
#             if visited[i] == 0 and minV > distance[i]:
#                 minV = distance[i]
#                 w = i
#         # 해당 리스트에서 가장 작은 비용 찾고 방문처리
#         visited[w] = 1

#         # 정점 v에 대해 
#         for v in range(N+1):
#             # w와 인접 노드이면서,
#             if 0 < graph[w][v] < 10000:
#                 # 시작정점에서부터 정점 w를 거쳐 v로 가는 비용과
#                 # 시작정점에서 v로 가는데 걸리는 비용중 최솟값 갱신
#                 distance[v] = min(distance[v], distance[w] + graph[w][v])

# N = int(input())
# M = int(input())

# INF = 100000
# graph = [[INF] * (N+1) for _ in range(N+1)]
# # 각 노드에 도착하는 최소 거리 기록
# distance = [0] * (N+1)

# for i in range(N+1):
#     # 자기 자신은 이동 불가하니 0으로 초기화
#     graph[i][i] = 0

# for _ in range(M):
#     s, e, w = map(int, input().split())
#     graph[s][e] = w
#     graph[e][s] = w

# # 찾을려는 구간 출발점과 도착번호
# start, end = map(int, input().split())
# dijkstra(start)
# print(distance[end])

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 6 25
2 4 46
3 5 18
3 4 34
4 5 40
6 4 51
'''

# # 임의의 정점에서 출발
# def dijkstra(now):
#     # 방문 정보 표기
#     visited = [0] * (V+1)
#     visited[now] = 1

#     # 인접 행렬 정보 기반, 첫 시작 지점에서 각 노드별 방문 가능 거리 기록
#     for next in range(V+1):
#         distance[next] = arr[now][next]

#     for _ in range(V):
#         w = 0
#         minV = 10000

#         for i in range(V+1):
#             if visited[i] == 0 and minV > distance[i]:
#                 minV = distance[i]
#                 w = i
#         visited[w] = 1

#         # 정점 v에 대해
#         for v in range(V+1):
#             # w와 인접 노드이면서,
#             if 0 < arr[w][v] < 10000:
#                 # 시작점점에서부터 정점 w를 거져 v로 가는 비용과
#                 # 시작지점에서 v로 가는데 걸리는 비용중, 최솟값 갱신
#                 distance[v] = min(distance[v], distance[w] + arr[w][v])



# # 노드, 간선
# V, E = map(int, input().split())
# # 인접행렬 정보
# # 최소 비용을 기록할 것이므로 첫 초기화시에는 최댓값으로 초기화
# arr = [[100000] * (V+1) for _ in range(V+1)]
# # 각 노드에 도착하는 최소 거리 기록
# distance = [0] * (V+1)

# for i in range(V+1):
#     # 내 위치 == 이동불가
#     arr[i][i] = 0

# for _ in range(E):
#     # 진출 노드, 진입 노드, 가중치
#     s, e, w = map(int, input().split())
#     # 무방향 그래프이므로 양쪽 노드 모두 진입/진출 노드
#     arr[s][e] = w
#     arr[e][s] = w
# dijkstra(0)
# print(distance)




# 임의의 정점에서 출발
def dijkstra(now):
    # 방문 정보 표기
    visited = [0] * (V+1)
    visited[now] = 1

    # 인접 행렬 정보 기반, 첫 시작 지점에서 각 노드별 방문 가능 거리 기록
    for next in range(V+1):
        distance[next] = arr[now][next]

    for _ in range(V):
        w = 0
        minV = 1e9

        for i in range(V+1):
            if visited[i] == 0 and minV > distance[i]:
                minV = distance[i]
                w = i
        visited[w] = 1

        # 정점 v에 대해
        for v in range(V+1):
            # w와 인접 노드이면서,
            if 0 < arr[w][v] < 1e9:
                # 시작점점에서부터 정점 w를 거져 v로 가는 비용과
                # 시작지점에서 v로 가는데 걸리는 비용중, 최솟값 갱신
                distance[v] = min(distance[v], distance[w] + arr[w][v])



# 노드, 간선
V = int(input())
E = int(input())
# 인접행렬 정보
# 최소 비용을 기록할 것이므로 첫 초기화시에는 최댓값으로 초기화
arr = [[] for _ in range(V+1)]
# 각 노드에 도착하는 최소 거리 기록
distance = [0] * (V+1)

for i in range(V+1):
    # 내 위치 == 이동불가
    arr[i][i] = 0

for _ in range(E):
    # 진출 노드, 진입 노드, 가중치
    s, e, w = map(int, input().split())
    # 무방향 그래프이므로 양쪽 노드 모두 진입/진출 노드
    arr[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])