# 입력
# 2개의 정수가 공백을 두고 입력된다.

# 출력
# 두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

n1, n2 = map(int, input().split())

if not bool(n1) and not bool(n2):
    print(True)
else:
    print(False)