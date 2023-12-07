# 리스트 배열, DP 구상이 어려워 코드 참고 (출처: https://yuna0125.tistory.com/124)

N = int(input())

t = []  # 상담 기간
p = []  # 상담 비용
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(N-1, -1, -1):  # 뒤에서부터 거꾸로
    if t[i] + i > N:  # 상담에 필요한 일수가 퇴사일을 넘어가면
        dp[i] = dp[i+1]  # 다음날 값 그대로 가져옴

    else:
        # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])
