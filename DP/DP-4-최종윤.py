#답지 확인
#import sys만 추가하면 됐었다. 이렇게 맞는다고?..

import sys
sys = input.stdin.readline

n = int(input())

#n에 따라 DP테이블?

counsel = [[0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    t, p = map(int,input().split())
    counsel[i][0] = t
    counsel[i][1] = p
    

dp = [0] * (n+1)


for i in range(1, n+1):
    exitT = i + counsel[i][0] - 1
    if exitT < n+1:
        if dp[exitT] < dp[i-1] + counsel[i][1]:
            dp[exitT] = dp[i-1] + counsel[i][1]
    if dp[i] == 0 or dp[i-1] > dp[i]:
        dp[i] = dp[i-1]

print(dp[n])
