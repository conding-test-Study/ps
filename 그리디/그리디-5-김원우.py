import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))
    ans = 0
    tmp = -1

    for i in range(len(prices)-1, -1, -1):
        if tmp >= prices[i]:
            ans += tmp-prices[i]
        else:
            tmp = prices[i]
    print(ans)

