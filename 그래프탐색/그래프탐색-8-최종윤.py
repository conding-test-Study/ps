# 답지 확인  특정 이동 횟수 제한 , 벽부수기 3차원 배열 기억하자  
# m,n  3차원배열 초기화 
import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
m,n = map(int,input().split())
arr= [list(map(int,input().split())) for i in range(n)]


dh = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        r,c,z = q.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][z] - 1
        #상하좌우 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if  nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if not visited[nr][nc][z] and not arr[nr][nc]:
                visited[nr][nc][z] = visited[r][c][z] +  1
                q.append([nr,nc,z])
        if z < k:
            for (i,j) in dh:
                nr = r + i
                nc = c + j
                if  nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if not arr[nr][nc]:
                    if not visited[nr][nc][z+1]:
                        q.append([nr,nc,z+1])
                        visited[nr][nc][z+1] = visited[r][c][z] + 1
    return -1

print(bfs())
            
            #아최단거리 visited에 거리 기록하면서 가는데 더 짧은거를 넣을때만 갱신하고
#말점프 써서먼저 저장된경우를 남겨두면 되겠다.
