# 1. 주사위는 1부터 6
# 2. 같은눈이 3개 >>> 10,000원 +(같은 눈)x1000원
# 3. 같은눈이 2개 >>> 1,000원 + (같은 눈)x100원
# 4. 모두 다른눈 가장 큰눈 x 100원

a, b, c = map(int, list(input().split()))
if a == b == c:
    print(10000 + a*1000)
elif a == b != c:
    print(1000 + a*100)
elif a != b == c:
    print(1000 + b*100)
elif a == c != b:
    print(1000 + a*100)
else:
    print(max(a,b,c)*100)
    