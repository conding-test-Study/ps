import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(12)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
def bfs(i, j, visited):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    color = graph[i][j]
    cnt = 1
    arr = []
    arr.append([i,j])

    while q:
        cur_i, cur_j = q.popleft()
        for k in range(4):
            new_i = cur_i + di[k]
            new_j = cur_j + dj[k]
            if 0 <= new_i < 12 and 0 <= new_j < 6:
                if visited[new_i][new_j] == 0 and graph[new_i][new_j] == color:
                    q.append([new_i,new_j])
                    visited[new_i][new_j] = 1
                    arr.append([new_i, new_j])
                    cnt += 1
    if cnt >= 4:
        for l in arr:
            graph[l[0]][l[1]] = '.' # 터뜨리기

    return cnt

def relocation(graph):
    for i in range(10,-1,-1):
        for j in range(6):
            if graph[i][j] != '.':
                new_i = i+1
                color = graph[i][j]
                while new_i < 12 and graph[new_i][j] == '.':
                    graph[new_i][j] = color
                    graph[new_i-1][j] = '.'
                    new_i += 1


ans = 0
while True:
    flag = 1
    for i in range(12):
        for j in range(6):
            visited = [[0] * 6 for _ in range(12)]
            cnt = 0
            if graph[i][j] != '.':
                cnt = bfs(i,j,visited)
                if cnt >= 4:
                    # 터진거 하나라도 있으면 반복문 계속 돌리게하기
                    flag = 0
    if flag == 1:
        break
    else:
        ans += 1
    relocation(graph)
print(ans)