# 시간초과와 메모리초과의 콜라보가 어마어마한 문제다
# 맨 처음에 DFS로 접근했는데 시간초과나서 BFS로 돌리고 방문처리 방식을 좀 수정해서 풀었음
# 근데 또 메모리초과나서 pypy로 제출했는데 정답처리됨.
# python3로는 뭔가 더 최적화해야 풀리는거 같은데... 걍 pypy로 만족..


import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int,input().split())
network = [[] for _ in range(n+1)]
ans = [0] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    network[b].append(a)

def bfs(startCom, computer, visited):
    global ans
    q = deque([])
    q.append(computer)
    visited[computer] = 1

    while q:
        curCom = q.popleft()
        for newCom in network[curCom]:
            if visited[newCom] != 1:
                visited[newCom] = 1
                q.append(newCom)
                ans[startCom] += 1

for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    bfs(i, i, visited)

maxCnt = max(ans)
for i in range(1, n+1):
    if maxCnt == ans[i]:
        print(i, end=" ")