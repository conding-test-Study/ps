# bfs 활용했으나, 테스트 케이스에서 계속 런타임 에러 발생
# m, n이 각각 어느 부분 원소를 가리키는지 파악하는 것이 중요.

from collections import deque


def solution(maps):
    m = len(maps)
    n = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        D = deque()
        D.append((x, y))

        while D:
            x, y = D.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print("지금 좌표: ", nx, ny)

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    # and visited[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    # visited[nx][ny] = 1
                    D.append((nx, ny))

        return maps[m-1][n-1]

    print(maps)

    answer = bfs(0, 0)

    if answer < 1:
        return -1
    else:
        return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
# print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
#       1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
