# 260000 총 금액
# 4 물건의 갯수
# 20000 5 갯수별 구매한 금액
# 30000 2
# 10000 6
# 5000 8

total_cost = int(input())
count = int(input())
price = []
cost = 0
for i in range(count):
    stuff = map(int, input().split())
    price.append(list(stuff))
    cost += (price[i][0] * price[i][1])

if total_cost == cost:
    print('Yes')
else:
    print('No')
