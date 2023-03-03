# 게임을 하는 사람의 수
N = int(input())

# 백트래킹을 하며 경우의 수를 구하기 위한 리스트
back_list = list(range(1, N+1))

# 한팀에 들어가는 사람의 수 => 경우의 수의 길이
P_num = N // 2
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [1] * N
total_result = []

# 경우의 수 구하기 1,2가 팀일때 / 1,3이 팀일때 ...
def back(i, k, res):
    global visited, total_result
    if i == k:
        total_result.append(res)
        return

    for j in range(N):
        if visited[j]:
            visited[j] = 0
            back(i+1, k, res+[back_list[j]])
            visited[j] = 1

back(0, P_num, [])
print(total_result)
