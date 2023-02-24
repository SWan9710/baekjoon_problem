N2_list =[]
N = int(input())    # 0 ~ 30000

# N2 = N에서 임의의 수를빼서 반복문을 돌려서 갯수가 최대가 되는것
i = 1
while i != N:
    N2 = N - i
    N2_list.append(N2)
    i += 1
print(N2_list)

# 3번째 수는 1번수와 2번수의 차이

# 4번째 수는 2번수와 3번수의 차이
# 음의 정수가 만들어 질때 stop

