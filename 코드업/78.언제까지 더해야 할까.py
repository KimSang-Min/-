# 입력
# 정수 1개가 입력된다.

# 출력
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

inputVar = int(input())
result = 0

for i in range(1, inputVar+1):
    result += i
    if result == inputVar or result >= inputVar:
        break

print(i)