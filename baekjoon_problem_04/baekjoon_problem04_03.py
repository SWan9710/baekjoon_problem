N = int(input())
X = map(int, input().split())
arr = []
for i in X:
    arr.append(i)    
arr.sort()
print(arr[0],arr[-1])