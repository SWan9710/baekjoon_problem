# 별찍기
star = int(input())

for i in range(star, 0,-1):
    print(' '*(i-1),end='')
    print('*'*(star-(i-1)))