# 알람 설정하기
# 첫째줄에 H와 M이 띄워서 주어짐 >> H시 M분 형태
# 입력시간은 24시간 형식
# 하루의 시작은 0:0 이고 끝은 23:59

H , M = map(int, input().split())
watch = M - 45
if H != 0:
    if watch > 0:
        print(f'{H} {watch}')
    elif watch == 0:
        print(f'{H} 0')
    else:
        H -= 1
        print(f'{H} {60-abs(watch)}')
else :
    if watch > 0:
        print(f'{H} {watch}')
    elif watch == 0:
        print('0 0')
    else:
        H = 23
        print(f'{H} {60-abs(watch)}')
