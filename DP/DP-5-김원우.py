# 답 찾아봄
# DP는 진짜 적응이 안된다..

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())
    dp = [0] * (m+1)

    for coin in coins:
        if coin > m:
            continue
        dp[coin] += 1
        for i in range(coin+1, m+1):
            dp[i] = dp[i-coin] + dp[i]
    print(dp[m])

