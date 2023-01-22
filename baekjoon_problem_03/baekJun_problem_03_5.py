import sys # input 으로 입력받을 경우 문자열을 하나씩 입력받아서 반복문이 길어질때 코드 로딩 속도가 느려짐
t = int(input())
for i in range(t):
    a,b = map(int, sys.stdin.readline().split()) #한줄 단위로 입력받고 맨끝 개행문자(\n) 문자도 같이 저장됨
    print(a+b)

    # 이를 피하기 위해서 sys.stdin.readline().rstrip()을 사용하여 맨끝 개행문자를 제거
    # 또한 입력받는 문자를 str 형식으로 받아오기 때문에 정수를 입력받을때는 형변환이 필요
