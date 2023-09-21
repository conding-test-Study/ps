#전에 풀었던 문제라 기억남 
#최댓값을 여러번 찾아서 그전 작은 값들과 뺴주는 것 
#뒤에서 부터 반복문

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    prices = list(map(int,input().split()))
    maxP = prices[len(prices) - 1]

    ans = 0
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] < maxP:
            ans += maxP - prices[i]
        else:
            maxP = prices[i]
    print(ans)
