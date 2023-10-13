#답지확인 
#deepcopy해서 1을 하나씩 전부 지워보는 것을 생각했으나 그거는 크기 작을때만 쓸수 있나보다 

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr= [list(map(int,list(input().rstrip()))) for i in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        r,c,broke = q.popleft()
        if r == n-1 and c == m-1:
            return visited[n-1][m-1][broke]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if  nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            
            if visited[nr][nc][broke] == 0 and arr[nr][nc] == 0:
                q.append((nr,nc,broke))
                visited[nr][nc][broke] = visited[r][c][broke] + 1
            elif broke == 0 and arr[nr][nc] == 1:
                q.append((nr,nc, 1))
                visited[nr][nc][1] = visited[r][c][0] + 1
    return -1

print(bfs())
