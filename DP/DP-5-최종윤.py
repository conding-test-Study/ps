#답지확인 https://bio-info.tistory.com/218
#처음 greedy로 품 - 틀림,  -> 완탐DFS로 시도함- 구현못함 -> 답지 확인 
#print(dp)를 출력해보니 이해에 도움이 됐다.

c, n = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
dp = [1e7 for _ in range(c + 100)] #dp[i]는 i명 증가할 때 최소 비용
dp[0] = 0 #0명 0원

for cost, num_people in city:#각 도시에 대해
    for i in range(num_people, c + 100):#n_p부터 c+100까지 최소비용 갱신
        dp[i] = min(dp[i - num_people] + cost, dp[i])# i명일 때, 최소비용 갱신
#i를 num_people 증가시켜서 도달한 경우와 이전 채워놓은 최소값과 비교

        
print(min(dp[c:]))          #c명이 아니라 c이상의 값에서 최소비용으로 도달하는 경우가 있을 수 있다.
