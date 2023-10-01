# 답지확인

#dfs 하면서 depth를 파라미터로 넘겨주는것을 모름
#입력할때 cctv 위치와 종류 저장해놓는것도 모름

#deepcopy?몰라

#한 방향으로 반복이동하는거 구현 몰라
#범위 벗어나지 않으면 하는걸로하면 무한루프에서 끝내는걸 다시해야함
#범위 벗어나면 벽이면 break로하면 무한루프로 한방향가면서 넘어가면 끝

#방향이 그냥 연결된거 다 뻗어가는게 아닌 특정 방향으로 가는거 몰라
#북동남서만 가지고하지 않고 짝지은 방향정보 배열을 하나 더 만들어서하면 더
#간결해지는듯


#빨리 답지볼걸.. 절대 못햇을듯 고민한다고해도 정보를 찾아보면서 해야지
#그냥 존재하는 유형 잘 풀 수 있도록 외우자 어려워,,

import copy
n, m = map(int,input().split())
cctv = [] #cctv 종류, x좌표, y좌표
board = [] #사무실 정보



for i in range(n):
    data = list(map(int,input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])
#티비가 있는지 매 입력마다 확인하여  종류와 위치를 저장
            
#============input======

#티비 방향 정보
mode = [
    [],
    [[0], [1], [2], [3]], #1 cctv ~
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],  # 5 cctv
]


# U R D L
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def fill(board, mode, r, c):
    for i in mode:
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                break
            if board[nr][nc] == 6:
                break
            elif board[nr][nc] == 0:
                board[nr][nc] = -1


def dfs(depth, board): #search
    global min_value
    if depth == len(cctv): # complete search
        count = 0
        for i in range(n): #find 0
            count += board[i].count(0)
        #update min
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(board) # copy board
    cctv_num, r, c = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, r, c)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(board) # init board

min_value = int(1e9)
dfs(0, board)
print(min_value)

