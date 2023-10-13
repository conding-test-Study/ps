# 0을 기준으로 BFS를 돌리면 된다는 아이디어를 생각해내면 간단한 BFS문제가 됨
import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(h)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt = 0
def bfs():
    q = deque()
    visited = [[0]*w for _ in range(h)]
    q.append([0, 0])
    visited[0][0] = 1
    melt_cnt = 0
    melt_list = []

    while q:
        cur_i, cur_j = q.popleft()
        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if visited[ni][nj] == 0:
                    if arr[ni][nj] == 0: # 공기인경우
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                    elif arr[ni][nj] == 1: # 치즈인경우
                        visited[ni][nj] = 1
                        melt_cnt += 1
                        melt_list.append([ni, nj])

    for cheese in melt_list: # 치즈 녹이기
        cur_i = cheese[0]
        cur_j = cheese[1]
        arr[cur_i][cur_j] = 0
    return melt_cnt

time = 0
while True:
    tmpCnt = bfs()
    if tmpCnt == 0:
        break
    else:
        cnt = tmpCnt
        time += 1
print(time)
print(cnt)