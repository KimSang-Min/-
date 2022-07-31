# 입력
# 2개의 정수가 공백을 두고 입력된다.

# 출력
# 하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.


n1, n2 = map(int, input().split())

if (bool(n1) == True) or (bool(n2) == True):
    print(True)
else:
    print(False)