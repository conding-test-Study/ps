#답지확인
#처음에 DFS완탐으로 풀었으나 시간초과  puddles 좌표 거꾸로된 것 신경 못써서 틀림
# 기본적인 DP문제라고 함, 목표까지 가능한 모든 최단거리 경우수 DP로 풀이
#시작지점부터 가능한 경우수를 계속 기록함 현재좌표에서 위 왼쪽에 있는걸 더해서 
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: 
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m] % 1000000007
