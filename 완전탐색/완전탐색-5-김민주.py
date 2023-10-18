import sys
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = []


def shape1(x, y):
    # 정사각형
    if x < N - 1 or y < M - 1:
        result = 0
        result += graph[x][y]
        result += graph[x+1][y]
        result += graph[x][y+1]
        result += graph[x+1][y+1]
        return result


# 각 모양을 전부 함수로 만든 뒤 반복문 돌리려고 했으나 너무 복잡해질 것이 우려됨
# DFS 1개 함수를 통해 모양 전부 커버하기 (출처: https://velog.io/@jajubal/파이썬백준-14500-테트로미노)
input = sys.stdin.readline


def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
