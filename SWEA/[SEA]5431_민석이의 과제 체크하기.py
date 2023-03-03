import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(range(1, N+1))
    people = map(int, input().split())
    for i in people:
        if i in arr:
            arr.remove(i)
    print(f'#{tc}',*arr)
