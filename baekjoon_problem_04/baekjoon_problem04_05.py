arr = []
arr2 = []
for i in range(28):
    a = int(input())
    arr.append(a)

for i in range(1,31):
    arr2.append(i)

for i in arr:
    arr2.remove(i)
arr2.sort()
print(arr2[0])
print(arr2[1])