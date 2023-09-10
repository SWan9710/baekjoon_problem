import sys
input = sys.stdin.readline

# A, B = map(str, input().split())
# result = 0

# for i in range(len(A)):
#     for j in range(len(B)):
#         result += int(A[i]) * int(B[j])

# print(result)

A, B = input().split()
A, B = sum(list(map(int, A))), sum(list(map(int, B)))
result = A * B
print(result)
