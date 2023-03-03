import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
# 입력받을때 언제까지 입력받는다가 없으므로 try문으로 받기
for i in range(6):
    delta, array = map(int, input().split())
    arr.append((delta, array))

while True:
    count = 0
    for i in range(1,len(arr)):
        if arr[0][0] == arr[i][0]:
            count += 1
    if count == 1:
        arr.append(arr.pop(0))
    else:
        break

# 밭이 꺽이는 부분
result = []
for i in range(4):
    if arr[i][0] == arr[i+2][0]:
        result.append(arr[i+1][1])

m_row = result[0]
m_col = result[1]
# 밭의 최대 넓이
row = 0
col = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > row:
            row = arr[i][1]
    else:
        if arr[i][1] > col:
            col = arr[i][1]

print(((row * col) - (m_row * m_col)) * N)