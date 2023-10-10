#답지 확인

# 몇초후에 터지는지 설치되는지 이해하는게 잘 안 됨
#t가 지나면서 일정 주기마다 반복적으로 나오는 결과를 저장하여 보여줄 생각을 못함

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def boom(arr):
    board = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                board[i][j] = '.'
                
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < R and 0 <= nc < C:
                        board[nr][nc] = "."
    return board

                

R,C,N = map(int,input().split())


arr = []
for i in range(R):
    arr.append(list(input().rstrip()))
    #4-5    4.1 폭발  5  9

temp = [['O'] * C for _ in range(R)]
    
if N == 1:
    for i in range(R):
        print(''.join(arr[i]))
elif N % 2 == 0:
    for i in range(R):
        print(''.join(temp[i]))
elif N % 4 == 3:    #2-3  3폭발   7 11
    boom1 = boom(arr)
    for i in range(R):
        print(''.join(boom1[i]))
        
elif N % 4 == 1:
    boom1 = boom(arr)
    boom2 = boom(boom1)
    for i in range(R):
        print(''.join(boom2[i]))
