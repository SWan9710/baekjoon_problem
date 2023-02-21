import sys
sys.stdin = open('input.txt')

# 첫줄은 총 단지의 갯수
# 둘째줄 부터 N 줄까지 단지의 수를 출력

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
rot_arr = list(map(list, zip(*arr)))

for i in range(N):
    print(arr[i])

print()
for i in range(N):
    print(rot_arr[i])
