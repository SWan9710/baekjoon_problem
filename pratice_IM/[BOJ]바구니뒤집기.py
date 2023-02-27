# N, M = map(int, input().split())
# arr = [0] * (N+1)
# for i in range(1,N+1):
#     arr[i] = i
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     temp = []
#
#     for k in range(i, j+1):
#         temp.append(arr[k])
#     temp = temp[::-1]
#     num = 0
#     for k in range(i, j+1):
#         arr[k] = temp[num]
#         num += 1
#
# print(*arr[1:])
while True:
    try:
        word = input()
        print(word)
    except EOFError:
        break