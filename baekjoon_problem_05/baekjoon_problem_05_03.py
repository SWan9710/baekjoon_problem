# 한수
<<<<<<< HEAD
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

N = int(input())
count = 0   # 등차수열의 갯수를 셀 변수
if N <= 99:  # N이 100보다 큰경우
    for i in range(N):
        count += 1

arr = []
if N > 99:
    count += 99
    for i in range(100, N+1):
        arr.append(str(i))
    
    for i in range(len(arr)):
        if int(arr[i][0]) - int(arr[i][1]) == int(arr[i][1]) - int(arr[i][2]):
            count += 1
print(count)
    
    
=======
N = int(input())

arr = []

for i in range(1,N+1):
    arr.append(i)

count = 0
for i in range(len(arr)): # 110
    new_arr = []
    for j in range(len(str(arr[i]))):
        new_arr.append(arr[i]%10)
        arr[i] //= 10

    # print(new_arr)
    if len(new_arr) == 1:
        count += 1
        continue
    
    total_arr = []
    for j in range(len(new_arr)-1):
        if new_arr[j] - new_arr[j+1] != 0:
            total_arr.append(new_arr[j] - new_arr[j+1])
    
    if len(total_arr) >= 2:
        for j in range(len(total_arr)-1):
            if total_arr[j] == total_arr[j+1]:
                count += 1
    
    else:
        count += 1


print(count)


>>>>>>> cea4d29e59afa09595d22ebc7d3547f7eda75053
