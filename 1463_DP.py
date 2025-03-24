# 백준 1463번: 1로 만들기
num = int(input())
cntList = [0] * (num+1)

for i in range(2, num+1):
    if i % 3 == 0:
        if cntList[i//3] <= min(cntList[i//2], cntList[i-1]):
            cntList[i] = 1 + cntList[i//3]

    if i % 2 == 0 and cntList[i] == 0 :
        if cntList[i//2] <= cntList[i-1]:
            cntList[i] = 1 + cntList[i//2]

    if cntList[i] == 0 :
      cntList[i] = 1 + cntList[i-1]

    print(f"{i}: {cntList[i]}")