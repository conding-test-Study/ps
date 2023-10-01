# DFS 활용 시도, 시간초과 발생

count = 0
counts = 0
pre_x, pre_y = 0, 0


def solution(n, computers):

    visited = [[0] * n for _ in range(n)]

    def dfs(x, y):
        global count
        global counts
        global pre_x, pre_y

        while x <= n-1:
            print("현재 좌표: ", x, y)
            print("전 좌표: ", pre_x, pre_y)
            counts += 1

            if pre_x > x:
                break
            # if counts >= count + n**2:
            #     break

            if y < n-1:
                if computers[x][y] == 1 and x < y and visited[x][y] != 1:
                    visited[x][y] += 1
                    print("change!")
                    count += 1
                    dfs(y, x)
                else:
                    pre_x = x
                    pre_y = y

                    visited[x][y] += 1
                    y += 1

            elif y == n-1:
                if computers[x][y] == 1 and x < y and visited[x][y] != 1:
                    visited[x][y] += 1
                    print("change!")
                    count += 1
                    dfs(y, x)
                else:
                    visited[x][y] += 1

                    pre_x = x
                    pre_y = y

                if x + 1 == n:
                    break
                else:
                    pre_x = x
                    pre_y = y

                    x += 1
                    y = 0

    dfs(0, 0)
    print(visited)
    print("거쳐온 좌표 수: ", counts)
    answer = n - count
    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# DFS 활용 예시 코드 (출처: https://daeun-computer-uneasy.tistory.com/70)


def solution2(n, computers):

    # DFS 함수는 visited에 도장 찍기만 함
    def dfs(v):
        visited[v] = True

        for nei in range(n):    # 인접노드 탐구
            # unvisited + computers에서 값 1 -> dfs 재귀함수 수행
            if not visited[nei] and computers[v][nei]:
                dfs(nei)

    # visited에 방문처리 안 된 노드 갖고 dfs 수행 & 수행횟수 체크
    count = 0
    visited = [False] * (n)

    for node_idx in range(n):

        if not visited[node_idx]:
            dfs(node_idx)   # k열의 j행: 'j'는 dfs 외부, 'k'는 dfs 내부에서 인덱스 카운트
            count += 1         # dfs 한묶음 끝나면 count 해주기

    return count
