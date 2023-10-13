# 발상은 예시 코드 참고 (출처: https://hongcoding.tistory.com/18)

from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        a, b, c = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽 없는 경우
            # 벽을 뚫어본 적이 없으면 visited[nx][ny][0], 있으면 visited[nx][ny][1]에 값 찍히도록 구성
            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

            # 벽을 처음으로 만난 경우 1회에 한정해서 뚫을 수 있게 함
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))


bfs(0, 0)
print(visited)

# 벽을 통과해본 경우는 result[1], 벽을 통과하지 않고 최단거리가 나온 경우는 result[0]에 저장
result = visited[N-1][M-1]

if result[0] == 0 and result[1] == 0:
    print(-1)
else:
    if result[0] < result[1]:
        print(result[0])
    else:
        print(result[1])
