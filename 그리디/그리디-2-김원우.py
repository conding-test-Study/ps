import sys
input = sys.stdin.readline

num = list(input())
num.pop() #개행 제거
max_ans = []
min_ans = []

cntM = 0 # M 갯수 세는 용도

for s in num:
    if s == "K":
        max_ans.append(str((10**(cntM)) * 5))
        cntM = 0
    else:
        cntM += 1

for i in range(cntM):
    # 더이상 K가 없다면 M을 이어서 붙이는 것 보다 떨어뜨려서 계산하는게 더 큰 숫자를 만들 수 있음
    max_ans.append("1")
cntM = 0
print("".join(max_ans))

for s in num:
    if s == "K": # K 나올 때 마다 이어붙인 M은 처리해주고 K는 따로 붙여주기
        if cntM != 0:
            min_ans.append(str(10 ** (cntM - 1)))
        min_ans.append("5")
        cntM = 0
    else:
        # M은 계속 이어 붙이기
        cntM += 1
if cntM != 0:
    min_ans.append(str(10 ** (cntM-1)))

print("".join(min_ans))
