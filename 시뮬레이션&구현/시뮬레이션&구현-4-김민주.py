# DFS로 풀려고 했으나, BFS 탐색과 DFS식 재귀를 합쳐놓고는 뎁스 카운팅을 못해서 멈춰버림
from collections import deque
import sys
field = []
for _ in range(12):
    field.append(input())

print(field)

visited = [[0]*6 for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def change_puyo(x, y, color, cnt):
    cnt += 1
    print("첫 좌표: ", x, y)
    print("지금까지의 카운트: ", cnt)
    visited[x][y] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        print("탐색 좌표: ", nx, ny)

        if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
            continue

        if visited[nx][ny] == 0:
            if field[nx][ny] != color:
                visited[nx][ny] += 1
            else:
                # cnt += 1
                print("지금까지의 카운트: ", cnt)
                visited[nx][ny] = visited[x][y] + 1
                change_puyo(nx, ny, color, cnt)

    # print("함수 종료 시까지 카운트: ", cnt)
    # print("함수 끝내는 지점의 값: ", visited[x+dx[3]][y+dy[3]])
    return cnt


for i in range(12):
    for j in range(6):
        if field[i][j] != '.' and not visited[i][j]:
            cnt = 0
            a = change_puyo(i, j, field[i][j], cnt)
            print("결과: ", a)
            # print("지금까지의 카운트: ", cnt)


# BFS + 방문처리가 맞았음. 큐 활용도 필요.
# 출처: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-11559-Puyo-Puyo-BFS
input = sys.stdin.readline


def check(x, y):
    q = deque([(x, y)])
    now = graph[x][y]
    pos = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            graph[i][j] = '_'
            bombList.append((i, j))


graph = [list(input().rstrip()) for i in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    bombList = []

    # 색이 같은 뿌요 4개 이상 모여있는 곳 있는지 체크해서 터뜨리기
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and graph[i][j] != '_' and not visited[i][j]:
                check(i, j)

    if len(bombList) == 0:
        break

    # 뿌요 내리기
    for bomb in bombList:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.'

    time += 1

print(time)
