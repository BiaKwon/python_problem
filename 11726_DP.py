# 백준 11726번: 2xn 타일링
# 다이나믹 프로그래밍 (실버 3)

n = int(input())
cntList = [0] * max(3, (n+1))   # cntList[i]: 2xi 크기 직사각형을 1x2, 2x1 타일로 채우는 방법의 수
cntList[1] = 1
cntList[2] = 2

# cntList[i] = cntList[i-1]+cntList[i-2]
for i in range(3, n+1):
    cntList[i] = cntList[i-1]+cntList[i-2]

print(cntList[n] % 10007)

