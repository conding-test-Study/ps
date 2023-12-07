# 답 참고
# knapsack 알고리즘 문제 중 하나임.

import sys
input = sys.stdin.readline

c, n = map(int,input().split())
cities = []

for i in range(n):
    cities.append(list(map(int,input().split())))
maxCost = float('INF')
dp = [maxCost for _ in range(c+100)]
dp[0] = 0

for city in cities:
    cost = city[0]
    benefit = city[1]
    for i in range(city[1], c+100):
        dp[i] = min(dp[i-benefit] + cost, dp[i])
print(min(dp[c:]))