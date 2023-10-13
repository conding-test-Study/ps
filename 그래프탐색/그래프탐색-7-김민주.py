# 7번 '치즈' 문제 풀이
# 아이디어 참고, 이후 직접 코드 구현
# 아이디어 출처: https://velog.io/@hygge/Python-백준-2636-치즈-BFS

from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque([(x, y)])

    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    melt = []

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            else:

                # graph 값이 0인 노드로 BFS를 돌리고
                # BFS 돌아가는 노드 인근에 graph 값이 1인 노드가 나오면 melt 리스트에 저장
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    melt.append([nx, ny])

    return melt


# cnt 변수에 시간 저장, cakes 변수에 녹은 치즈 수 저장
# 치즈를 다 녹인 뒤 녹은 치즈 수를 변수 저장하여 결과 출력 용이하게 만듦

cnt = 0
cakes = 0
while True:

    m = bfs(0, 0)
    if len(m) > 0:
        cakes = len(m)
        for a in m:
            i, j = a
            graph[i][j] = 0
        cnt += 1
        cakes = len(m)
    else:
        break


print(cnt)
print(cakes)
