# 입력
# 2개의 정수가 공백을 두고 입력된다.

# 출력
# 두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

n1, n2 = map(int, input().split())

if (bool(n1) and (not bool(n2))) or (bool(n2) and (not bool(n1))):
    print(True)
else:
    print(False)