# 입력
# 정수 1개가 입력된다.
# -2147483648 ~ +2147483647, 단 0은 입력되지 않는다.

# 출력
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D 를 출력한다.


inputVar = int(input())

if (inputVar < 0) and (inputVar % 2 == 0):
    print('A')
elif (inputVar < 0) and (inputVar % 2 != 0):
    print('B')
elif (inputVar > 0) and (inputVar % 2 == 0):
    print('C')
else:
    print('D')