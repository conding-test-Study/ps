# 탑다운 방식
# DP가 아직 안익숙해서 답지봄

import sys
input = sys.stdin.readline

n = int(input())
sc = []

for i in range(n):
    sc.append(list(map(int,input().split())))
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담X
    if i + sc[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1], dp[i + sc[i][0]] + sc[i][1])

print(dp[0])