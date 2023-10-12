# 빡구현에 정신을 잃을뻔함
# bfs돌면서 국경열리는 국가들 그룹화하고 인구수 넣어주기

import sys
from collections import deque
input = sys.stdin.readline

n, L, R = map(int,input().split())
world = [list(map(int, input().split())) for _ in range(n)]
day = 0

def bfs(i, j, visited):
    global day, world
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    open = [[i, j]]
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    po = world[i][j]
    flag1 = 0
    cnt = 1
    while q:
        cur_i, cur_j = q.popleft()
        for k in range(4):
            new_i = cur_i + di[k]
            new_j = cur_j + dj[k]
            if 0 <= new_i < n and 0 <= new_j < n and visited[new_i][new_j] == 0:
                diff = abs(world[cur_i][cur_j] - world[new_i][new_j])
                if L <= diff <= R:
                    q.append([new_i, new_j])
                    open.append([new_i, new_j])
                    visited[new_i][new_j] = 1
                    po += world[new_i][new_j]
                    cnt += 1
                    flag1 = 1

    # BFS로 국경열리는 국가들 open배열에 넣고 인구수 계산해서 떄려박기
    if flag1 == 1:
        poRes = po // cnt
        for o in open:
            cur_i = o[0]
            cur_j = o[1]
            world[cur_i][cur_j] = poRes
    return flag1

while True:
    visited = [[0] * n for _ in range(n)]
    flag = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                flag.append(bfs(i, j, visited))
    if 1 in flag:
        day += 1
    else:
        # BFS돌면서 국경열리는 국가 단 하나도 안나오면 stop
        break
print(day)

