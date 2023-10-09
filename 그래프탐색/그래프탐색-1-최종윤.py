#답지 5개 확인했는데 다 시간초과?
import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)


def bfs(node):
    visited = [False]*(n+1)
    q = deque()
    q.append(node)
    cnt = 0
    visited[node] = True

    while q:
        v = q.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt

result = []
for i in range(1, n+1):
    result.append(bfs(i))

max = max(result)
for i in range(len(result)):
    if max == result[i]:
        print(i+1, end=' ')

