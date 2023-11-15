T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    w = [0]
    c = [0]
    for i in range(N):
        wi, ci = map(int, input().split())
        w.append(wi)
        c.append(ci)
    for i in range(1, N + 1):
        for wk in range(1, K + 1):
            if wk < w[i]:
                dp[i][wk] = dp[i-1][wk]
            else:
                dp[i][wk] = max(dp[i-1][wk], dp[i-1][wk-w[i]] + c[i])
    answer = dp[N][K]
 
    print("#{} {}".format(tc, answer))

