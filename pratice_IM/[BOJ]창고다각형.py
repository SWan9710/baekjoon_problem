arr = []
N = int(input())
for i in range(N):
    L, H = map(int, input().split())
    arr.append((L, H))

arr.sort()
print(arr)
result = 0
for i in range(1, N):
    num1 = (arr[i][0] - arr[i-1][0])
    num2 = (arr[i-1][1])
    result+= num1 * num2
print(result)