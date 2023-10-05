from collections import deque

def solution(maps):
    n = len(maps) - 1
    m = len(maps[0]) - 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([0,0])
    while(q):
        x,y = q.popleft()
        # if x == n and y ==m:
        #     return maps[n][m]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n+1 or ny < 0 or ny >= m+1:
                continue
#     벽이 아니라면 maps가 0이 아니라면 
            if maps[nx][ny] == 0:
                continue
    # 방문하지 않은 노드인경우 
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
                    
    if maps[n][m] == 1:
        return -1
    else:
        return maps[n][m]   
