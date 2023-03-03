import sys
sys.stdin = open('input.txt')

bingo_board = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]

print(bingo_board)
print(answer)

def search(bingo_board, answer):
    bingo = 0
    bingo_count = 0

    # 정답판의 숫자 가져오기
    for i in range(5):
        for j in range(5):

            # 빙고판의 숫자 가져오기
            for ii in range(5):
                for jj in range(5):

                    # 빙고판의 숫자가 정답판의 숫자와 일치할때
                    if bingo_board[ii][jj] == answer[i][j]:
                        # 사용되지 않는 수인 -1로 변경
                        bingo_board[ii][jj] = -1
                        # 현재 몇번째만에 빙고가 완성되는 지 세기위한 카운드수
                        bingo_count += 1

                        while True:
                            num