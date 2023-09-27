# 답지 확인

# 재귀 생각 못하고 반복문으로만 했다가   3개로 나눴을때 다시 같은 연산 3개 나누는거 할 때 구현이 어려웠음 

#cnt를 반환하도록 했었는데 3개로 나누는 것을 할 때  가위 2개 위치 정하는 거를 반복문으로 하는데  가위 한가지 위치만 가지고 연산한다음  return해버려서 

# 전역변수를 계속 cnt와 비교해서 최소 최대를 구함 그리고 void return 

import sys


def cnt_odd(n):
    cnt = 0
    for c in n:
        if int(c) % 2 == 1:
            cnt += 1
    return cnt

def func(n, cnt):
    print(n, cnt)
    cnt += cnt_odd(n)
    if len(n) == 1:
        ans[0] = min(ans[0], cnt)
        ans[1] = max(ans[1], cnt)
        return

    elif len(n) == 2:
        func(str(int(n[0]) + int(n[1])), cnt)

    elif len(n) >= 3:
        tmp = []
        for i in range(1,len(n)-1):
            for j in range(i+1, len(n)):
                func(str(int(n[:i]) + int(n[i:j]) + int(n[j:])), cnt)
        



n = input()
ans = [sys.maxsize, -sys.maxsize]
func(n, 0)

print(ans[0], ans[1])
