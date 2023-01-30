num = int(input())
number = map(int, input().split())
v = int(input())
count = 0
for i in number:
    if v == i:
        count +=1
print(count)
