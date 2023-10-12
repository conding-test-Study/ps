# 아이디어 구상 자체를 하지 못하여 답 코드 참고함
# 출처: https://ddiyeon.tistory.com/82


import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
visit = [[0]*m for i in range(n)]

# 연결된 0인 칸 탐색 후 테두리 개수 반환


def dfs(y, x):
    stack = [(y, x)]
    visit[y][x] = 1
    cnt = 0
    while stack:

        # 테두리 구하는 경우의 각 칸별 디테일을 직접 나열하고, 디테일의 갯수를 카운팅하기
        y, x = stack.pop()
        if y % 2:
            di = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, 0), (1, -1)]
        else:
            di = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        for i, j in di:
            if y+i >= 0 and y+i < n and x+j >= 0 and x+j < m and not visit[y+i][x+j]:
                if board[y+i][x+j]:
                    cnt += 1
                else:
                    visit[y+i][x+j] = 1
                    stack.append((y+i, x+j))
    return cnt


# 가장 바깥쪽 칸들과 연결된 칸 탐색
total = 0
for y in [0, n-1]:  # 맨 위, 맨 아래 줄 탐색
    for x in range(m):
        if board[y][x]:
            total += 2
            if (y == 0 and x == m-1) or (y == n-1 and x == 0):
                total -= 1
        elif board[y][x] == 0 and not visit[y][x]:
            total += dfs(y, x)
for y in range(n):  # 맨 오른쪽, 맨 왼쪽 줄 탐색
    for x in [0, m-1]:
        if board[y][x]:
            if (x == 0 and y % 2) or (x == m-1 and y % 2 == 0):
                total += 3
            else:
                total += 1
        elif board[y][x] == 0 and not visit[y][x]:
            total += dfs(y, x)

print(total)
