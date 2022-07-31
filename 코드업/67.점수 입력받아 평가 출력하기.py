# 입력
# 정수(0 ~ 100) 1개가 입력된다.

# 출력
# 평가 결과를 출력한다.

inputVar = int(input())

if (100 >= inputVar >= 90):
    print('A')
elif (89 >= inputVar >= 70):
    print('B')
elif (69 >= inputVar >= 40):
    print('C')
else:
    print('D')