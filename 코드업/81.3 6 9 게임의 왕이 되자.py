# 입력
# 30 보다 작은 정수 1개가 입력된다.
# (1 ~ 29)

# 출력
# 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
# 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.

n = int(input())

for i in range(1, n+1):
    if '3' in str(i):
        i='X'
        print(i, end=" ")
    elif '6' in str(i):
        i='X'
        print(i, end=" ")
    elif '9' in str(i):
        i='X'
        print(i, end=" ")
    else:
        print(i, end=" ")
    