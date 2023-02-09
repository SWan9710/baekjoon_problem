# 한수
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


