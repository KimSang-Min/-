# 입력
# 정수 1개가 입력된다.
# (0 ~ 100)

# 출력
# 1부터 그 수까지 짝수만 합해 출력한다.

from re import I


inputVar = int(input())
result = 0

for i in range(1, inputVar+1):
    if i%2==0:
        result += i

print(result)