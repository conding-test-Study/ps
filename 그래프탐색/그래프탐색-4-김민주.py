# BFS 활용 길찾기 + 시간체크 로직 만듦
# but 그람 뽑은 경우 / 그렇지 않은 경우 구분해서 함수 만들기 어려웠음


import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

print(graph)

visited = [[0]*M for _ in range(N)]


def bfs(x, y, found):

    queue = deque([(x, y)])
    # visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # found = False

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny] == 0:

                if graph[nx][ny] == 1:
                    if found == False:
                        continue
                    elif found == True:
                        visited[nx][ny] = visited[a][b] + 1
                        queue.append((nx, ny))

                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append((nx, ny))

                # graph[nx][ny] == 2 나오면, 그 이후로는 1이 의미가 없어짐
                # 이걸 어떻게 구현하지?
                if graph[nx][ny] == 2:
                    found = True
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append((nx, ny))


visited[0][0] = 1
bfs(0, 0, False)
print(visited)

result = visited[N-1][M-1]

if 0 < result <= T+1:
    print(result-1)
else:
    print("Fail")


# 예시코드 (출처: https://velog.io/@hygge/Python-백준-17836-공주님을-구해라-BFS)
# 칼 사용 경우와 그렇지 않은 경우 중 최단시간 구하기
input = sys.stdin.readline


def bfs(x, y, dst_x, dst_y, time):
    q = deque([(x, y, time)])
    visited = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1 and not visited[nx][ny]:
                if nx == dst_x and ny == dst_y:
                    return time+1
                visited[nx][ny] = 1
                q.append((nx, ny, time+1))
    return float('inf')


n, m, t = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
    if 2 in graph[i]:
        # 칼 위치 따로 좌표 빼놓기
        knife = [i, graph[i].index(2)]

# 칼 사용 X
not_use_knife = bfs(0, 0, n-1, m-1, 0)

# 칼 사용 O
# 칼 나오기 전까지의 시간 + 그 이후의 시간 더하기
tmp = bfs(0, 0, knife[0], knife[1], 0)
if tmp != float('inf'):
    use_knife = tmp + abs(n-1 - knife[0]) + abs(m-1 - knife[1])
else:
    use_knife = tmp

ans = min(not_use_knife, use_knife)
print(ans if ans <= t else 'Fail')
