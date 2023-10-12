from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

n,m,t = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

visited = [[0]*m for _ in range(n)]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    ans = sys.maxsize
    while q:
        r,c = q.popleft()
        if arr[r][c] == 2:
            ans = visited[r][c] -1 + (n-1) - r + m-1 - c
        if r == n-1 and c == m-1:
            return min(visited[r][c] - 1, ans)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] != 1 and visited[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = visited[r][c] + 1
    return ans


ans = bfs(0,0)


if ans > t :
    print("Fail")
else:
    print(ans)
