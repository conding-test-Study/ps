# 아이디어 참고
# 앞선 공주구하기 문제나 벽부수기 문제처럼 상태가 두개가 아니라 여러개의 상태가 존재해서 해결방법을 떠올리지 못했음
# 해결방법은 visited 배열을 3차원으로 사용하는 것이었다.

import sys
from collections import deque
input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

dki = [-2, -2, 2, 2, -1, -1, 1, 1]
dkj = [-1, 1, -1, 1, -2, 2, -2, 2]

k = int(input())
w, h = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(h)]
def bfs():
    q = deque()
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    q.append([0,0,0])
    visited[0][0][0] = 1
    minCnt = sys.maxsize

    while q:
        cur_i, cur_j, move = q.popleft()
        if cur_i == h-1 and cur_j == w-1:
            minCnt = min(minCnt, visited[cur_i][cur_j][move])

        for p in range(4): # 일반이동
            ni = cur_i + di[p]
            nj = cur_j + dj[p]
            if 0 <= ni < h and 0 <= nj < w:
                if arr[ni][nj] != 1 and visited[ni][nj][move] == 0:
                    q.append([ni,nj,move])
                    visited[ni][nj][move] = visited[cur_i][cur_j][move] + 1

        if move < k:
            for p in range(8):
                ni = cur_i + dki[p]
                nj = cur_j + dkj[p]
                if 0 <= ni < h and 0 <= nj < w:
                    if arr[ni][nj] != 1 and visited[ni][nj][move+1] == 0:
                        q.append([ni,nj,move+1])
                        visited[ni][nj][move+1] = visited[cur_i][cur_j][move] + 1
    return minCnt-1 if minCnt != sys.maxsize else -1
print(bfs())