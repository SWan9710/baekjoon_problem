# 윤년 구하기
# 조건 1. 4의 배수이며
    # 조건 1.1 100의 배수가 아니다
# 조건 3. 또는 400의 배수이다

year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print('윤년')
        else:
            print('윤년이 아니다.')
else:
    print('윤년이 아니다.')