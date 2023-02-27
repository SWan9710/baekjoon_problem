# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 
# 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오

N, M  = map(int, input().split())

# 입력받은 N을 이용하여 1부터 N+1 까지 배열 만들기
lst = list(range(1, N+1))
# 중복제거를 위한 visited 배열 만들기
visited = [1] * N

# 입력받는 i 값, 조건범위, 결과를 저장할 res
def f(i, k, res):
    global visited
    # i 값은 lst의 인덱스 값
    if i == k:
        print(*res)
        return
    # 입력받은 N 만큼 반복문을 돌때
    for j in range(N):
        # 방문기록이 있을때
        if visited[j]:
            # 방문기록을 초기화 하고
            visited[j] = 0
            # i + 1번째의 함수를 다시 불러옴
            # 결과값에 lst의 j번째 값을 추가해줌
            f(i + 1, k, res+[lst[j]])
            # 위의 함수 불러온게 끝났다면 방문기록을 다시 초기화
            visited[j] = 1

# 리스트 시작이 0부터 M 까지 불러오고 결과를 배열로 저장
f(0, M, [])
