# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def printGraph(graph):
    print("graph")
    for i in graph:
        print(*i)
    print("@@@@@@@@@@@")

def bfs(i, j):
    global today
    res = deque()
    q = deque()
    res.append((i, j))
    q.append((i, j))

    cnt = 1
    sum = graph[i][j]

    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[i][j] = True
    today[i][j] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N or visit[nx][ny] or today[nx][ny]: continue

            gap = abs(graph[x][y]-graph[nx][ny])
            if L <= gap <= R:
                q.append((nx, ny))
                res.append((nx, ny))
                visit[nx][ny] = True
                today[nx][ny] = True
                cnt += 1
                sum += graph[nx][ny]

    if cnt != 1:
        for x, y in res:
            graph[x][y] = sum//cnt  # 인구수 조정

    return cnt

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


ans = 0

while True:
    # 예외처리
    # 하루에 동시에 이동 가능한 그룹이 2개 이상일 경우

    # 4 10 50
    # 10 100 20 90
    # 80 100 60 70
    # 70 20 30 40
    # 50 20 100 10 에서

    # 10 100 50 50
    # 50 50 50 50
    # 50 50 50 50
    # 50 50 100 50 로 바뀌고 다음 날

    # (30) 100 50 50
    # (30) 50 50 50
    # 50 50 (50) 50
    # 50 (50) (100) (50) 괄호친 부분이 동시에 다 바뀌어야 하는데,
    # 윗 그룹만 바뀌고 아래 그룹은 안바뀜..

    # -> today 배열로 오늘 바뀐애들은 더이상 못건들게 처리

    today = [[False for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            tmp = bfs(i, j)
            if tmp != 1:    # 한번이라도 이동이 있으면
                # printGraph(graph)
                flag = 1

    # 종료 조건 : 한번도 인구 조정이 일어나지 않았을 경우
    printGraph(graph)
    if flag == 0:
        break
    else: ans += 1

printGraph(graph)
print(ans)