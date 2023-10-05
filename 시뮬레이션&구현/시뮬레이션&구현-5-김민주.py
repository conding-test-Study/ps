# 숫자 1-3-2-5 등 연달아 발생하는 결과를 어떻게 다뤄야할지 몰라서 막힘
# 아래는 예시코드 (출처: https://developer-ellen.tistory.com/53)

import copy
n, m = map(int, input().split())
cctv = []
graph = []
# 1, 2, 3, 4일 때 나아가야 하는 방향의 인덱스를 mode에 전부 저장함
# mode에 저장된 인덱스는 dx[i], dy[i]의 형태로 적용
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 일단 graph를 입력값으로 채우고, cctv 위치는 따로 저장
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

# graph 탐색 함수


def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

# 재귀함수로 그래프 채워지는 흐름 구현


def dfs(depth, arr):
    global min_value

    # cctv 다 끝났을 때 최솟값 구하고 함수 끝내기
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    # temp 값 만들기 (DFS 문제에서 꽤 쓰이는 테크닉)
    temp = copy.deepcopy(arr)

    # cctv 번호별로 graph 탐색 + dfs 진행
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)
