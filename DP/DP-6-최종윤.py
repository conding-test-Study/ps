#답지 확인
#knapsack  coins n개 세로     목표 무게 0 ~ m가로    세로와 가로에 무얼 두어야할지
#그리고 dp식을 세우지 못함  coin 0개 ~ k개골라서 w가 된 경우 수를 [0][0]에서 계속 더해서 구한다.
#[1][w] 부터는 w-coins[i] 에서 coins[i]더해서 올수있으면 [i-1][w-coins[i]] 값씩 계속 더해서 구한다.
#coin값 배수에 계속 k 증가시켜 나가면서 갱신하는거 생각 못함

t = int(input())
for t_c in range(t):
    n = int(input())
    coins = [0] + list(map(int,input().split()))
    m = int(input())
    dp = [[0] * (m+1) for _ in range(n + 1)]
    dp[0][0] = 1

    def knapsack():
        for i in range(1, n + 1):
            for w in range(m + 1):
                k = 0
                while w - k * coins[i] >= 0:
                    dp[i][w] += dp[i-1][w- k*coins[i]]
                    k += 1
        print(dp[n][m])


    knapsack()
