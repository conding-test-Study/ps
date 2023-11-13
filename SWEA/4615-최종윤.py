# 일직선상 같은 것이 있는 것을 어떻게 확인할까 ? 했는데 cctv감시랑 비슷했다 느낌이
# 일직선상 계속 움직이면서 채우는것 뿐만아니라 확인도 가능하다

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
# N x N 배열 생성  가운데에 WB BW가 배치 가운데는 N//2 - 1 , N//2  4:1,2   6: 2,3  8: 3,4
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2

    dr = [-1, 1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]
    for _ in range(M):
        #입력에 가로 세로 위치 값 순서로 들어옴 행열이 아님
        c, r, color = map(int,input().split())  # 1 w  , 2 B
        r, c = r - 1, c - 1 
        # c, r 에 놓으면 
        data = []
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            while True:
                if not (0 <= nr < N and 0 <= nc < N):
                    data = []
                    break
                if board[nr][nc] == 0: # 빈 칸인 경우
                    data = []
                    break
                if board[nr][nc] == color: # 같은 돌인 경우
                    break
                else:
                    data.append([nr,nc])  # 다른 돌인 경우
                nr, nc = nr + dr[i], nc + dc[i]
            # data에 넣어놓은 다른돌을 모두 바꾼다.
            for xr, xc in data:
                board[xr][xc] = color
        board[r][c] = color

    w_cnt, b_cnt = 0, 0
    for i in range(N):
        w_cnt += board[i].count(2)
        b_cnt += board[i].count(1)
  
    print("#{} {} {}".format(tc, b_cnt, w_cnt))

