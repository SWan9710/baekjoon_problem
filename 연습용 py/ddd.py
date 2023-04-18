import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())

time = []
for _ in range(N):
    si, ei = map(int, input().split())
    time.append([si, ei])

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
# 시작 시간과 종료시간 입력받고 종료시간 기준으로 정렬
####################################

# print('----time----')
# print(time)
# print()

# 회의실 넣어줄거 생성
# 회의실의 첫번째 회의는 종료시간이 가장 짧은 회의
# 가장먼저 종료되는 회의를 넣어주고
meeting = []
heappush(meeting, time[0][1])

# 1부터 반복하며 비교
for i in range(1, N):
    # 현재 회의가 종료 되지 않았을때 다음 회의가 시작되어야 하는경우
    if time[i][0] < meeting[0]:
        # 다음 회의의 종료시간을 방에 넣어줌
        heappush(meeting, time[i][1])
    # 현재 회의가 종료되고 다음 회의가 시작되는 경우
    else:
        # 현재 회의가 끝났으니 방에서 빼주고
        # 다음회의의 종료시간을 넣어줌
        heappop(meeting)
        heappush(meeting, time[i][1])

# 남은 회의의 갯수수
print(len(meeting))