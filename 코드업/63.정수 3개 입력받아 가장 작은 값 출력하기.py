# 입력
# 3개의 정수가 공백으로 구분되어 입력된다.
# -2147483648 ~ +2147483648

# 출력
# 가장 작은 값을 출력한다.

n1, n2, n3 = map(int, input().split())

print((n1 if n1 < n2 else n2) if (n1 if n1 < n2 else n2) < n3 else n3)