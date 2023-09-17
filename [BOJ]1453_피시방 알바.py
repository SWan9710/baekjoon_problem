N = int(input())
num = list(map(int, input().split()))
numSet = set(num)
print(len(num) - len(numSet))