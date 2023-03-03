import sys
sys.stdin = open('input.txt')

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # 겹치는 부분이 없을때
    # 첫번째 사각형의 오른쪽 끝점이 두번째 사각형의 왼쪽 끝점보다 작거나
    # 반대인 경우
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1 :
        print('d')
        continue
    # 점 한개만 겹치는 경우
    # 꼭짓점이 서로 맞다은 경우
    if (p1 == x2 and q1 == y2) or (p2 == x1 and q2 == y1) or (p1 == x2 and q2 == y1) or (p2 == x1 and y2 == q1) :
        print('c')
        continue

    # 한 변이 만날때
    if p1 == x2 or p2 == x1 or q1 == y2 or q2 == y1:
        print('b')
        continue

    # 그 외의 모든 경우는 사각형이 겹치는 경우
    else:
        print('a')
        continue