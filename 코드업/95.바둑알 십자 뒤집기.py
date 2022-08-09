# 입력
# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

# 출력
# 십자 뒤집기 결과를 출력한다.

d = []
for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)

for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if d[x-1][j] == 1: 
            d[x-1][j] = 0
        else: 
            d[x-1][j] = 1

        if d[j][y-1] == 1: 
            d[j][y-1] = 0
        else: 
            d[j][y-1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()