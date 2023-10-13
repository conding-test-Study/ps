# 공주문제랑 비슷한듯?
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = []
for i in range(n):
    tmp = list(input().strip())
    tmp2 = []
    for num in tmp:
        tmp2.append(int(num))
    arr.append(tmp2)
def pr(a):
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print()
def bfs():
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    q = deque()
    visited = [[0]*m for _ in range(n)]
    visited_wall = [[0]*m for _ in range(n)]
    q.append([0,0,0]) # i, j, 벽부수기 썼는지 안썼는지
    visited[0][0] = 1
    arr[0][0] = 1

    while q:
        cur_i, cur_j, wall = q.popleft()
        # print(f"cur_i = {cur_i}, cur_j = {cur_j}, wall = {wall}")
        # pr(arr)
        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]
            if ni == n-1 and nj == m-1:
                if arr[ni][nj] > arr[cur_i][cur_j] + 1 or arr[ni][nj] == 0:
                    arr[ni][nj] = arr[cur_i][cur_j] + 1
                continue
            if 0 <= ni < n and 0 <= nj < m:
                if wall == 1 and visited_wall[ni][nj] == 0: # 벽부수기 씀
                    if arr[ni][nj] == 1: # 벽인경우
                        continue
                    elif arr[ni][nj] == 0:
                        q.append([ni,nj,1])
                        visited_wall[ni][nj] = 1
                        arr[ni][nj] = arr[cur_i][cur_j] + 1
                    else:
                        # if arr[ni][nj] >= arr[cur_i][cur_j] + 1:
                        q.append([ni,nj,1])
                        visited_wall[ni][nj] = 1
                        arr[ni][nj] = arr[cur_i][cur_j] + 1
                elif wall == 0 and visited[ni][nj] == 0: # 안씀
                    if arr[ni][nj] == 1: # 벽인경우
                        q.append([ni,nj,1])
                        visited[ni][nj] = 1
                        arr[ni][nj] = arr[cur_i][cur_j] + 1
                    elif arr[ni][nj] == 0:
                        q.append([ni,nj,0])
                        visited[ni][nj] = 1
                        arr[ni][nj] = arr[cur_i][cur_j] + 1
                    else:
                        # if arr[ni][nj] >= arr[c?ur_i][cur_j] + 1:
                        q.append([ni,nj,0])
                        visited[ni][nj] = 1
                        arr[ni][nj] = arr[cur_i][cur_j] + 1
bfs()


if arr[n-1][m-1] == 0:
    print(-1)
else:
    print(arr[n-1][m-1])

