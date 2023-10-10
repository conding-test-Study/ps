# 1초-2초-3초-4초 등 시간 흐름에 따른 주기 설정이 어려웠음

import sys
from collections import deque

R, C, N = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(str, input())))

print(graph)

visited = [[0]*C for _ in range(R)]


def bfs():
    cnt = 0

    D = deque()

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                D.append((i, j))

    cnt += 1

    while D:
        a, b = D.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = '.'

        cnt += 1


def break_bomb():
    for i in range(R):
        for j in range(C):
            bfs(i, j)


def make_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'


cnt = 1
while cnt <= N:
    print(cnt)

    if cnt == 1:
        cnt += 1

    if cnt == 2:
        make_bomb()
        print(graph)
        cnt += 1

    if cnt == 3:
        break_bomb()
        cnt += 1

    # else:


for g in graph:
    print(''.join(g))

# 예시코드 (출처: https://velog.io/@tunaman95/백준-16918번-봄버맨-Python)
# 결국 '짝수초에 폭탄 설치, 홀수초에 폭발' 패턴으로 문제를 해석하여 풀게 됨
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

R, C, N = map(int, input().rstrip().split())

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

# 폭탄이 모두 폭발한다.
# BFS는 '폭발' 파트만 담당


def bfs(q, board):
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx >= 0 and nx < R and ny >= 0 and ny < C and board[nx][ny] == 'O':
                board[nx][ny] = '.'


def simulate(t):
    global q, board
    if t == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i, j))
    elif t % 2 == 1:
        # 3초가 지난 폭탄을 폭발시킨다.
        bfs(q, board)
        # 3초후에 터질 폭탄을 q에 다시 저장한다.
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i, j))
    else:
        # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
        board = [['O']*C for _ in range(R)]


for i in range(1, N+1):
    simulate(i)

for i in board:
    print(''.join(i))
