# 처음에는 dfs를 시도했으나 오답 발생
# BFS로 구하는 문제였음 (참고: https://reliablecho-programming.tistory.com/107)
# 시간초과 주의

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

coms = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    coms[b].append(a)

print(coms)

cnt = 0

# visited = [False for _ in range(N+1)]


# def dfs(x):
#     global cnt

#     if len(coms[x]) > 0:

#         for c in coms[x]:
#             if visited[c] == True:
#                 return False

#             if visited[c] == False:
#                 visited[c] = True
#                 cnt += 1
#                 dfs(c)

#     return False


def bfs(x):
    global cnt
    # cnt = 0
    visited = [False for _ in range(N+1)]

    queue = deque()
    queue.append(x)

    visited[x] = True
    cnt += 1

    while queue:
        q = queue.popleft()

        for c in coms[q]:
            if visited[c] == False:
                visited[c] = True
                queue.append(c)
                cnt += 1


result = []

for i in range(1, N+1):
    # visited[i] = True
    # cnt += 1
    # dfs(i)
    bfs(i)
    result.append(cnt)
    cnt = 0
    # visited = [False for _ in range(N+1)]


# result.sort(key=lambda x: x[1], reverse=True)
print(result)

max = max(result)


for j in range(len(result)):
    if max == result[i]:
        print(i+1, end=' ')
