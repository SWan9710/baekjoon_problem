import sys
while True:
    ttt = input()

    # print(ttt)
    # 종료조건 end 입력시 while 문 종료
    if ttt == 'end':
        break

    # X 가 승리하는 조건
    if ttt.count('X') - ttt.count('O') == 1:
        # 판을 모두 채우는 경우는 X가 O보다 1많을때 뿐
        if ttt.count('X') + ttt.count('O') == 9:
            print('valid')
            continue
        # X가 1많을때 가로로 틱택토 완성 검사
        for i in range(0,9,3):
            if ttt[i] == 'O' and ttt[i+1] == 'O' and ttt[i+2] == 'O':
                print('invalid')
                break

        for i in range(0,9,3):
            if ttt[i] == 'X' and ttt[i+1] == 'X' and ttt[i+2] == 'X':
                print('valid')
                break

        # 왼쪽 대각선 검사
        if ttt[0] =='X' and ttt[4] == 'X' and ttt[8] =='X':
            print('valid')
            continue
        # 오른쪽 대각선 검사
        if ttt[2] =='X' and ttt[4] == 'X' and ttt[6] =='X':
            print('valid')
            continue
        for i in range(3):
            if ttt[i] == 'O' and ttt[i+3] == 'O' and ttt[i+6] == 'O':
                print('invalid')
                break




    if ttt.count('O') - ttt.count('X') == 0:
        for i in range(3):
            if ttt[i * 3:i * 3 + 3] == 'OOO':
                print('valid')
                break
        if ttt[0] == 'O' and ttt[4] == 'O' and ttt[8] == 'O':
            print('valid')
            continue
        if ttt[2] == 'O' and ttt[4] == 'O' and ttt[6] == 'O':
            print('valid')
            continue
        for i in range(3):
            if ttt[i] == 'O' and ttt[i+3] == 'O' and ttt[i+6] == 'O':
                print('valid')
                break
        else:
            print('invalid')
    else:
        print('invalid')