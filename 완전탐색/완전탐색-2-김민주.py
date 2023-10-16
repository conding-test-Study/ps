# 단순 상하좌우 탐색까지는 짜냈는데, 최소 값이 나오는 특정 케이스를 잡아내는 방법은 구상하지 못함

import sys
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

print(graph)
visited = [[False]*N for _ in range(N)]


def find_sum(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sum = graph[x][y]
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return False

        if visited[nx][ny] == True:
            return False
            # continue

        if not visited[nx][ny]:
            sum += graph[nx][ny]
            visited[nx][ny] = True

    return sum


result = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and cnt < 3:
            r = find_sum(i, j)
            if type(r) == int:
                print(r)
                print("좌표: ", i, j)
                result += r
                cnt += 1
            else:
                continue


print("답: ", result)


# 주로 DFS로 풀이 (출처: https://amor-fati.tistory.com/120)
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())   # 화단 한 변 길이
garden = [list(map(int, input().split())) for _ in range(n)]   # 화단 지점당 가격

# 꽃 심을수 있는지 알아보기


def check(i, j, visited):
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
        x, y = i + dx, j + dy
        if not ((0 <= x < n and 0 <= y < n) and visited[x][y]):
            return False
    return True

# 땅값 계산하기


def calc(i, j):
    cost = 0
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
        x, y = i + dx, j + dy
        cost += garden[x][y]
    return cost


def dfs(x, cnt, visited, cost_sum):
    global min_cost

    # 3회 체크시 끝내기
    if cnt == 3:
        min_cost = min(min_cost, cost_sum)
        return
    for i in range(x, n-1):
        for j in range(1, n-1):

            # 측정 가능한 경우, dfs를 돌리고 방문체크를 하기
            if check(i, j, visited):
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
                    visited[i + dx][j + dy] = False
                dfs(i, cnt+1, visited, cost_sum + calc(i, j))
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
                    visited[i + dx][j + dy] = True


min_cost = sys.maxsize
dfs(1, 0, [[True for _ in range(n)] for _ in range(n)], 0)
print(min_cost)
