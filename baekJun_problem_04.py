# 사분면 구하기
# (x, y)의 값이 주어짐
# (양수, 양수) >>> 1사분면
# (양수, 음수) >>> 4사분면
# (음수, 음수) >>> 3사분면
# (음수, 양수) >>> 2사분면

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
elif x < 0:
    if y > 0:
        print('2')
    else:
        print('3')