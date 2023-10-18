#답지 확인
# arr 가장 큰 값으로 나머지 횟수를 더해도 현재 나온 최대값보다 작거나 같은 경우 더이상 하지 않고 return하도록 했는데     
#이걸 백트래킹이라고 하는것 같다. 이 조건이 없으면 시간초과가 발생했다 차이가 많이 나는듯. 

#그리고 다른 풀이 중에 ㅗ모양 블록을 따로 반복문 돌려서 추가하는게 있었는데 합쳐서 
# cnt==2일때 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개 
#r,c cnt=2 에서    북 좌표 방문처리하고 값도 추가하고 cnt+1 
#똑같이 r,c cnt=3에서 다른 미방문 좌표 방문하고 값더해주면 cnt=4에서 return하고   visited=False
#다시 r,c,cnt=3 돌아와서 다른 좌표로 cnt=4방문하고 또 visited=false 
#현재 가지의 cnt=3에서 모두 방문했으니 

cnt=4  cnt=4  cnt=4V  cnt=4V
        cnt=3
                          cnt=4
cnt=3    cnt=2          cnt=3   cnt=4
                          cnt=4

# r,c에서 인접한 하나 골라놓고 나머지 한개를 r,c에서 인접한걸 골라서 cnt=4를 하도록 depth4에서 가능한 모든 탐색을 하기 위해 
#visited=true  dfs()  visited=false 똑같이 

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, arr))
max_total = 0

def dfs(r, c, total, cnt):
    global max_total
    if total + max_val * (4-cnt) <= max_total:
        return
    if cnt == 4:
        max_total = max(max_total, total)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            if cnt == 2:
                visited[nr][nc] = True # 탐색기록
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                dfs(r, c, total + arr[nr][nc], cnt + 1)
                visited[nr][nc] = False # 탐색기록 제거
            visited[nr][nc] = True
            dfs(nr, nc, total + arr[nr][nc], cnt + 1)
            visited[nr][nc] = False






for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = False

print(max_total)
    
