from collections import deque

N, L, R = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


# 그래프 전체를 탐색하며 visited[i][j]를 0 이상으로 만들기
# visited[i][j]의 값은 연합 번호
def make_union(x, y, num, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    sum = graph[x][y]
    visited[x][y] = num
    cnt = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            else:
                if visited[nx][ny] == 0:
                    now = graph[a][b] - graph[nx][ny]

                    if L <= abs(now) <= R:
                        visited[nx][ny] = num
                        sum += graph[nx][ny]
                        cnt += 1
                        queue.append((nx, ny))
                    else:
                        continue

    # 탐색 완료 후, 연합이 생기면 그 연합의 평균 인구 구하기
    if cnt > 1:
        avr = sum // cnt
        return avr
    else:
        return 0


def find_union_avr():
    li = [0 for _ in range(N**2)]

    num = 1
    visited = [[0]*N for _ in range(N)]

    # 연합 번호 매겨주기
    # 연합 번호별 평균값을 li에 저장
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if num < N**2:
                    li[num] = make_union(i, j, num, visited)
                    num += 1

    # 연합 번호를 다 매긴 뒤, 연합 번호가 같은 것끼리 같은 평균으로 graph의 값 바꿔주기
    how = 0
    for i in range(1, N**2):
        avr = li[i]
        if li[i] != 0:

            for j in range(N):
                for k in range(N):
                    if visited[j][k] == i:
                        graph[j][k] = avr

            how += 1

    if how > 0:
        return True
    else:
        return False


# 앞서 말한 절차를 연합 더만들수 없을 때까지 반복하기
# 반복 횟수 days가 답
days = 0
while True:

    if find_union_avr() == True:
        days += 1
        print("지금까지 날수: ", days)
        print(graph)

    else:
        break

print(days)
