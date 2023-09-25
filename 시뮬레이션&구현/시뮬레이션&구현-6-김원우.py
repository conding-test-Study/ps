# bfs의 기본개념을 알면 별로 어렵지 않게 풀 수 있는 문제였음
from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def bfs(i, j):
        q = deque()
        q.append([i, j])
        visited[i][j] = 1

        while q:
            cur_i, cur_j = q.popleft()
            if cur_i == n - 1 and cur_j == m - 1:
                break

            # print(f"cur_i = {cur_i} , cur_j = {cur_j}")

            for k in range(4):
                new_i = cur_i + di[k]
                new_j = cur_j + dj[k]

                if -1 < new_i < n and -1 < new_j < m:
                    if maps[new_i][new_j] != 0 and visited[new_i][new_j] == 0:
                        q.append([new_i, new_j])
                        maps[new_i][new_j] = maps[cur_i][cur_j] + 1
                        visited[new_i][new_j] = 1

    bfs(0, 0)
    if maps[n - 1][m - 1] == 1:
        answer = -1
    else:
        answer = maps[n - 1][m - 1]
    return answer