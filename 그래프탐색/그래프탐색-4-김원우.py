# 그람 들고있을때랑 안들고있을때 분리하는거 구현하기가 살짝 까다로웠음
from collections import deque
import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
castle = [list(map(int,input().split())) for _ in range(n)]
castle[n-1][m-1] = 1000000000
def bfs():
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    visited = [[0]*m for _ in range(n)]
    visited_gram = [[0]*m for _ in range(n)]

    q = deque()
    if castle[0][0] == 2:
        q.append([0,0,1])
        visited_gram[0][0] = 1
    else:
        q.append([0,0,0]) # i, j, 그람유무
        visited[0][0] = 1

    while q:
        cur_i, cur_j, gram = q.popleft()

        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if gram == 1 and visited_gram[ni][nj] == 0: # 그람이 있는경우
                    if ni == n-1 and nj == m-1:
                        castle[ni][nj] = min(castle[ni][nj], castle[cur_i][cur_j] + 1)
                        continue
                    if castle[ni][nj] == 1: # 벽인경우
                        visited_gram[ni][nj] = 1
                        castle[ni][nj] = castle[cur_i][cur_j] + 1
                        q.append([ni,nj,gram])
                    else:
                        visited_gram[ni][nj] = 1
                        castle[ni][nj] = castle[cur_i][cur_j] + 1
                        q.append([ni,nj,gram])

                elif gram == 0 and visited[ni][nj] == 0: # 그람이 없는경우
                    if ni == n - 1 and nj == m - 1:
                        castle[ni][nj] = min(castle[ni][nj], castle[cur_i][cur_j] + 1)
                        continue
                    if castle[ni][nj] == 2: # 그람인 경우
                        visited[ni][nj] = 1
                        castle[ni][nj] = castle[cur_i][cur_j] + 1
                        q.append([ni,nj,1])
                    elif castle[ni][nj] == 0:
                        visited[ni][nj] = 1
                        castle[ni][nj] = castle[cur_i][cur_j] + 1
                        q.append([ni,nj,gram])

bfs()
if castle[n-1][m-1] > t:
    print("Fail")
else:
    print(castle[n-1][m-1])

