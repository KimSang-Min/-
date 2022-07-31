# 입력
# 두 정수 a, b가 공백을 두고 입력된다.
# -2147483648 <= a, b <= +2147483647

# 출력
# a와 b가 다른 경우 True 를, 그렇지 않은 경우 False 를 출력한다.

a, b = map(int, input().split())

if b != a:
    print(True)
else:
    print(False)