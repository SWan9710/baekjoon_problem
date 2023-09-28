import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
temp = set(words)
words = list(temp)
words.sort()
words.sort(key=len)
for word in words:
    print(word)