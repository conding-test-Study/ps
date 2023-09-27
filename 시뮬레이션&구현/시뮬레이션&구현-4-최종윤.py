# list(input())하면 문자열"1234" -> 문자열 배열['1','2','3','4'] 몰랐음  문자열 . 변경 불가했음
# 4개이상 이동했을때 그 전에 이동한거 삭제했어야했는데 이전 좌표를 [].append 해놓는걸 모름
from collections import deque



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r,c):

    q = deque()
    q.append((r,c))

    boom = deque()
    boom.append((r,c))

    visited[r][c] = True
    cnt = 1
    flag = 0
    
    while q:
        r,c =  q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and arr[r][c] == arr[nr][nc]:
                q.append((nr,nc))
                boom.append((nr,nc))
                visited[nr][nc] = True
                cnt += 1
    if cnt >= 4:
        flag = 1

        for r,c in boom:
            arr[r][c] = "."
    return flag

def down():
    for i in range(6):
        rotate_queue = deque()
        for j in range(11,-1,-1):
            if arr[j][i] != '.':
                rotate_queue.append(arr[j][i])
    
        for j in range(11,-1,-1):
            if rotate_queue:
                arr[j][i] = rotate_queue.popleft()
            else:
                arr[j][i] = '.'
        


arr = []
for _ in range(12):
    arr.append(list(input().rstrip()))

result = 0
while True:
    chk = 0

    visited = [[False] * 6 for _ in range(12)]
    
    for i in range(6):
        for j in range(12):
            if arr[j][i] != ".":
                chk += bfs(j,i)
    down()

    if chk == 0:
        break
    else:
        result += 1
print(result)

