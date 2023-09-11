# N^2풀이에서 최적화 방법을 떠올리지 못해 정답 구글링함
import sys
input = sys.stdin.readline

n = int(input())
arr = []
stk = []
cnt = 0

for i in range(n):
    arr.append(int(input()))

for b in arr:
    while stk and stk[-1] <= b:
        stk.pop()

    stk.append(b)
    cnt += len(stk)-1
# 스택에서 현재 빌딩높이보다 작은것들은 다 빼주고 현재 빌딩보다 높은 빌딩들만 남겨놓음
# 스택길이 = 현재 빌딩의 옥상을 볼 수 있는 빌딩의 개수
print(cnt)
