N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = []
cnt = K-1

for i in range(N):
    # 리스트 길이가 짧아진 경우
    if K > len(arr):
        for k in arr:
            arr.append(k)
    else:
        while cnt < len(arr):
            result.append(arr.pop(cnt))
            cnt += K-1
        cnt = K-1

print(result)
