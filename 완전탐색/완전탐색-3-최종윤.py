#답지확인
#세다가 5되면 바로 break하려니까 그렇지 왼쪽 오른쪾 다 포함해서 세면 cnt 6이 될텐데 왜 틀린거지?

#왼쪽위 같이 탐색하면 6목 잡을수있는거 아니야? 같이 세서 6목이면
# 안 하면 되는 거잖아  대신 visited는  고려해야겠지 

import sys
input = sys.stdin.readline

# 오른쪽아래 왼쪽위로 연속으로있는 개수 세기
#오른쪽위 왼쪽아래로 연속 개수 세기
#가로 연속 세기
#세로 연속 세기
#이렇게 4가지로 처음 셌었는데 오른쪽 아래로 내려가는 방향만 하면 되네 왼쪽 위에서 부터 하니까  
#앞에 있는 건 다시 6목 체크하니까

        
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
                if 0 <= r + dr < 19 and 0 <= c + dc < 19 and arr[r][c] == arr[nr + dr][nc + dc]:
                    break
                print(arr[r][c])
                print(r+1, c+1)
                sys.exit(0)
            nr += dr
            nc += dc
print(0)
        

