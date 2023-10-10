import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

n,L,R = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))


def bfs(r,c):
    q = deque()
    q.append((r,c))
    tmp = []
    tmp.append((r,c))
    cnt = 0
    total = 0
    while q:
        r,c = q.popleft()
        total += arr[r][c]
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc))
                        tmp.append((nr,nc)) 
    total //= cnt
    
    if cnt > 1:
        while tmp:
            r,c = tmp.pop()
            arr[r][c] = total
    
    return cnt


# 더 연합할 수 없을때 까지
# cnt 2이상인것이 없을 때  그만둔다.
result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs(i,j) > 1:
                    flag = True
    if not flag:
        print(result)
        break
    result += 1
                
