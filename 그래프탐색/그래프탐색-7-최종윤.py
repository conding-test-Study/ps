import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr= [list(map(int,(input().split()))) for i in range(n)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    cnt = 0
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if  nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            #인접좌표에 0이 있다면 1을 지운다 다음 bfs때는 0이 되야함 -1로했다가 -1인걱 전부0으로
            #visited에 지운거 1로 기록
            #아니면 0으로하고 visited=1로해서  visited==0인 0이 인접할때만 
        
            if visited[nr][nc] == 0:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    visited[nr][nc] = 1
                    cnt += 1
                elif arr[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
    return cnt
            


#모든 좌표에 대해 bfs를 한번씩 x 테두리
#초기화하고 모든 좌표에 대해 다시 bfs하려면 visited초기화,그리고 순환 안 하기 위해 방문 필요
repeat = 0
total = 0
while True:
    cnt = 0
    visited = [[0] * m for _ in range(n)]

        #bfs했을때 녹은것이 아무것도 없을때까지
        #원본을 유지하거나 
        #내가 지운 1은 0이 되지 않고 한번 bfs에 적용되지 않아야 -1로?
    cnt += bfs(0,0)

    if cnt == 0:
        print(repeat)
        print(total)
        break
    else:
        repeat += 1
        total = cnt

#다시 0탐색하는걸로 구현할려니까 하기싫다.
#내가 인접한 0이 치즈 안쪽에있는건지 바깥쪽인지 어떻게 알아

#0입장에서 bfs돌렸을때 경계값을 접촉한적있다면 바깥아닌가?
        #경계값은 무조건 0이다
        #그리고 경계값 +1인곳에 놓인구멍은 바깥공기 취급
#따라서 0을탐색해서 경계값이랑 인접한지로는

#그럼 경계선에있는 0값을 탐색해서 이에 인접한 1을 지우고 지운 1을 센다?  금방 하네?
