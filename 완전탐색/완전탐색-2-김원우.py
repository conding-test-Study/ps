# 아이디어를 구현으로 못옮겼음
# 이런 유형의 완탐 백트래킹이 익숙하지 않아서 더 연습해야할듯

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

answer = sys.maxsize
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def check(i, j, visited):
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if not ((0 <= ni < n and 0 <= nj < n) and visited[ni][nj] == 0):
            return False
    return True

def visit_process(i, j, visited,flag):
    if flag == 0:
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            visited[ni][nj] = 1
    else:
        visited[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            visited[ni][nj] = 0
def calc(i, j):
    cost = arr[i][j]
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        cost += arr[ni][nj]
    return cost

def flowers(x, price, cnt, visited):
    global answer
    if price > answer: # 가지치기
        return
    if cnt == 3:
        answer = min(answer, price)
        return

    for i in range(x, n-1):
        for j in range(1, n-1):
            if check(i, j, visited):
                visit_process(i, j, visited, 0)
                flowers(i, price+calc(i,j), cnt+1, visited)
                visit_process(i, j, visited, 1)

flowers(1,0,0,[[0]*n for _ in range(n)])
print(answer)