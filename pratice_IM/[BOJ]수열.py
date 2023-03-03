import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
arr = list(map(int, input().split()))
# 누적합배열 생성하기 위해 sum1 배열에 초기값 넣어주기
# 누적합의 범위가 K로 주어지니 초기값은 처음부터 K 까지의 합
sum1 = [sum(arr[:K])]
# 누적합의 범위 K 보다 작거나 많은 범위를 가져오면 안되기 때문에 전체범위 N에서 누적합의 범위 K 만큼 빼주는거
for i in range(N - K):
    # 겹치는 범위 만큼은 연산을 안해야 속도가 빨라짐
    # 누적합은 0 - 5까지 더한 결과라고 할때 다음 누적값은 1 - 6 까지 이므로 기존의 누적값에서 첫번째 값을 빼주고
    # 다음에 오는 값만 더해주면 됨
    # sum1[i] <= 기존의 누적값 / arr[i] <= 첫번째 값 / arr[i+K] <= 다음에 넣어줄 값
    # 결과를 sum1에 넣어주기
    sum1.append(sum1[i] - arr[i] + arr[K+i])

print(max(sum1))