# DFS + 카운팅으로 풀었으나 오답
# 엣지케이스 요건 섬세하게 고려하기 어려웠음

import sys

graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))

visited = [[False]*19 for _ in range(19)]

# 방향 쓰기
direction = [(1, 0), (-1, 0), (0, 1), (0, -1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]

# DFS로 카운팅하기


def dfs(x, y, di):
    global cnt
    cnt += 1
    visited[x][y] = True
    print("현재 좌표: ", x, y)

    # if cnt < 5:

    dx, dy = direction[di]
    nx = x + dx
    ny = y + dy
    print(nx, ny)

    if 0 <= nx < 19 and 0 <= ny < 19:
        if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
            dfs(nx, ny, di)
        else:
            print("end")
            return False


cnt = 0
for i in range(19):
    for j in range(19):

        # 첫 노드 찾기 + 디렉션
        if cnt < 5:
            if graph[i][j] == 1 or graph[i][j] == 2 and not visited[i][j]:
                visited[i][j] = True
                print(i, j)
                cnt += 1

                for d in range(8):
                    dx, dy = direction[d]
                    nx = i + dx
                    ny = j + dy
                    if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                        continue

                    if graph[nx][ny] == graph[i][j] and not visited[nx][ny]:
                        dfs(nx, ny, d)

                        # if rs == "end":
                        # 루프 멈추기
                        if cnt == 5:
                            print("yeah")
                            print(graph[i][j])
                            print(i+1, j+1)
                            # for루프 전체 끝내기 코드
                            sys.exit(0)

                        if cnt < 5 or cnt >= 6:
                            cnt = 0
                            continue

print(0)


# 정답 코드 (출처: https://ywtechit.tistory.com/150)
# DFS 아닌 일반 완전탐색 + 카운팅으로만 처리
n = 19
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 0, -1]  # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]


def omok():
    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    while 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny]:
                        cnt += 1

                        if cnt == 5:
                            # 육목 판정 1
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:
                                break
                            # 육목 판정 2
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and arr[x][y] == arr[x - dx[i]][y - dy[i]]:
                                break
                            return arr[x][y], x+1, y+1  # 육목이 아닌 오목이면 return

                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1  # 승부가 나지 않을 때


color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)
