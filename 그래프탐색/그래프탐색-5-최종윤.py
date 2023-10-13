#답지 확인

https://ddiyeon.tistory.com/82
#연결된 노드를 가리키기위해 dr dc를 적절히 변형한다.
#탐색하고자하는 노드 주변 노드를 어떻게 drdc로 나타낼수있는지
#연결된 노드가 짝수 홀수에 따라 변하는

#1의 바깥 모서리의 개수가 의미하는것이
#0 이 인접하는 1칸의 개수 에다가
#짝수 홀수 아래 위에 따라 추가적으로 더해주면 된다는걸 생각 못함

#존재하는 칸마다 값을 구해  경우를 나누어 본다.
import sys
input = sys.stdin.readline

w,h = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

def dfs(r,c):
    stk = [(r,c)]
    visited[r][c] = True#!
    cnt = 0
    
    while stk:
        r,c = stk.pop()
        if r % 2:
            di = [(-1,0), (0,1), (1,0), (0,-1), (-1,-1), (1,-1)]
        else:
            di = [(-1,0), (0,1), (1,0), (0,-1), (1,1), (-1,1)]
        for dr, dc in di:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stk.append((nr,nc))
                elif arr[nr][nc] == 1:
                    cnt += 1
    return cnt

total = 0
#맨 윗줄 아랫줄
for i in [0, h-1]:
    for j in range(w):
        if arr[i][j] == 1:
            total += 2
            if (i == 0 and j == w-1) or (i == h-1 and j == 0):
                total -= 1
        elif arr[i][j] == 0 and not visited[i][j]:
            total += dfs(i,j)

#맨 왼쪽 오른쪽
for i in range(h):
    for j in [0, w-1]:
        if arr[i][j] == 1:
            if (i % 2 and j == 0) or (i % 2 == 0 and j == w-1):
                total += 3
            else:
                total += 1
        elif arr[i][j] == 0 and not visited[i][j]:
            total += dfs(i,j)

print(total)
