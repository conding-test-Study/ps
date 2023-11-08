#테스트케이스 98개 중 93개 맞았다는데 답지보고 수정하다가 39, 40 라인을 33라인으로 위치 바꾸니까 맞았다.
#기존 코드는 벽일떄는 머리가 바뀌었지만  범위 밖으로 나갈 때는 머리를 바꾸지 못했다... 순서가 어디갈지 여기저기 대보고 맞는거를...
# dict사용 스쳐갔는데 안 적어놓고 까먹음 , 
#s 문자-> 1 숫자( idx로 사용 ) -> ^문자  ,       
#com문자를 숫자에 대응시켜 dr,dc의 idx로 사용 가능하다.
#나는 com에 해당하는 idx를 찾기 위해 for문을 돌렸다.
            
T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    arr = []
    for i in range(H):
        data = list(input())
        arr.append(data)
        for j in range(W):
            if data[j] in ['^', 'v', '<', '>']:
                r, c = i, j

    n = int(input())
    commands = list(input())
#U D L R
    shape = ['^', 'v', '<', '>']
    command = ['U' ,'D', 'L', 'R']
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        if arr[r][c] == shape[i]:
            d = [dr[i], dc[i]]


    for com in commands:
        for i in range(4):
            if com == command[i]:
                nr = r + dr[i]
                nc = c + dc[i]
                d = [dr[i], dc[i]]
                car = shape[i]
                #arr[r][c] = car
                if 0 <= nr < H and 0 <= nc < W:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = car
                        arr[r][c] = '.'
                        r, c = nr, nc
                    #else:
                    #    arr[r][c] = car
                    

        if com == 'S':
            tmp_r = r
            tmp_c = c
            while True:
                nr = tmp_r + d[0]
                nc = tmp_c + d[1]
                if nr < 0 or nr >= H or nc < 0 or nc >= W:
                    break
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
                elif arr[nr][nc] == '#':
                    break
                tmp_r, tmp_c = nr, nc
        
            
#방향 어떻게 저장?
        #direction = 'U' or -> [dr[0], dc[0]]



    print("#{}".format(tc), end = ' ')
    for i in range(H):
        print(''.join(arr[i]))
