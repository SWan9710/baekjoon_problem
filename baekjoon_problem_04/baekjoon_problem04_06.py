arr = []
for i in range(10):
    x = int(input())
    y = x % 42
    if y not in arr:
        arr.append(y)
print(len(arr))