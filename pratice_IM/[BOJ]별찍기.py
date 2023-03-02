N = int(input())
M = (2*N)-1
i = 0
while N != 1:
    print(' '*(N-1),end='')
    print('*'*(i*2+1),end='')
    print()
    N -= 1
    i += 1

n = 0
while i != -1:
    print(' '*n,end='')
    print('*'*(i*2+1),end='')
    print()
    i -= 1
    n += 1