#답지확인
# 왼쪽 오른쪾 다 포함해서 세면 cnt 6이 될텐데 왜 틀린거지?


import sys
input = sys.stdin.readline

d = [[1,1], [-1,1], [0,1], [1,0]]


arr = []
loc = []
for i in range(19):
    data = (list(map(int,input().split())))
    for j in range(19):
        if data[j] != 0:
            loc.append([i, j])
    arr.append(data)

chk = False
for r,c in loc:
    for dr, dc in d:
        cnt = 1
        nr = r + dr
        nc = c + dc
        while 0 <= nr < 19 and 0 <= nc < 19 and arr[nr][nc] == arr[r][c]:
            cnt += 1
            if cnt ==5:
                if 0 <= r - dr < 19 and 0 <= c - dc < 19 and arr[r][c] == arr[r - dr][c - dc]:
                    break
                if 0 <= nr + dr < 19 and 0 <= nc + dc < 19 and arr[r][c] == arr[nr + dr][nc + dc]:
                    break
                print(arr[r][c])
                print(r+1, c+1)
                sys.exit(0)
            nr += dr
            nc += dc
print(0)


#틀린 코드
# 전에 풀었던 문제는 조합을 combi나 비트연산으로 만들었지만 이건 경우가 많으니 dfs가 좋지 않을까?



import sys
input = sys.stdin.readline

# 오른쪽아래 왼쪽위로 연속으로있는 개수 세기

#오른쪽위 왼쪽아래로 연속 개수 세기


#가로 연속 세기

#세로 연속 세기


def dfs(r, c, d):
    global cnt
    visited[r][c] = True
    cnt += 1

    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 19 and 0 <= nc < 19:
            if not visited[nr][nc] and arr[r][c] == arr[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, d)
        




#10x10을 탐색 세번 하는 거니까 100 ^3이 아니라 x3같은데 나올수있는 경우는^3이지만

d = [
    [[1,1], [-1,-1]],
    [[-1,1], [1,-1]],
    [[0,1], [0,-1]],
    [[1,0], [-1,0]],
]

arr = []
loc = []
for i in range(19):
    data = (list(map(int,input().split())))
    for j in range(19):
        if data[j] == 1 or data[j] == 2:
            loc.append([i, j])
    arr.append(data)

chk = False
for r,c in loc:
    for mode in d:
        visited = [[False]*19 for i in range(19)]
        cnt = 0
        dfs(r, c, mode)
        if cnt == 5:
            print(arr[r][c])
            print(r+1, c+1)
            chk = True
            break
    if chk:
        break
if not chk:
    print(0)
        
        
