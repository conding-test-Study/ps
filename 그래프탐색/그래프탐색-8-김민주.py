# visited[nx][ny][z] 를 만들고, z가 K 미만일 때까지 '말' 처럼 움직이기 가능하게 하는 아이디어
# 출처: https://velog.io/@ms269/백준-1600-말이-되고픈-원숭이-파이썬-Python
# 현재 코드로 시간초과 발생하나 이유를 예시 코드들에서 찾지 못함

from collections import deque

K = int(input())
W, H = map(int, input().split())

graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))


visited = []
for _ in range(H):
    visited.append([[0]*(K+1) for _ in range(W)])


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        a, b, c = queue.popleft()
        print("현재의 좌표: ", a, b, c, visited[a][b][c])

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

            if graph[nx][ny] == 1 and visited[nx][ny][c] == 0:
                if c + 1 <= K:
                    li = [[-2, -1], [-2, 1],
                          [-1, -2], [-1, 2], [1, -2], [1, 2], [-1, -2], [-1, 2]]
                    for l in li:
                        d, f = l
                        cx = a + d
                        cy = b + f

                        if cx < 0 or cx >= H or cy < 0 or cy >= W:
                            continue
                        if graph[cx][cy] == 0 and visited[cx][cy][c] == 0:
                            visited[cx][cy][c+1] = visited[a][b][c] + 1
                            queue.append((cx, cy, c+1))

                        else:
                            continue

            else:
                continue


bfs(0, 0)
print(visited)

result = visited[H-1][W-1][K]

if result > 0:
    print(result - 1)
else:
    print(-1)
