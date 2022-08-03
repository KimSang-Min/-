# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

# 출력
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

n1 = int(input())
n2 = input().split()

for i in range(n1):
    n2[i] = int(n2[i])

list = []

for i in range(24):
    list.append(0)

for i in range(n1):
    list[n2[i]] += 1

for i in range(1, 24):
    print(list[i], end=" ")