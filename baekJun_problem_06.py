# 1. 첫째 줄에는 현재시각이 공백으로 표기
# 2. 23시 59분까지 표기되며 지나면 0시0분이 된다.
# 3. 시간이 분단위로 주어진다.

time = list(map(int, input().split()))
cooking_time = int(input())
count = 0

if cooking_time + time[1] < 60:
    print(time[0], time[1]+cooking_time)

elif cooking_time + time[1] >= 60:
    count = (cooking_time + time[1]) // 60
    if time[0] + count >= 24:
        print(time[0]+count - 24, time[1]+cooking_time-(60*count))
    else:
        print(time[0]+count, time[1]+cooking_time-(60*count))