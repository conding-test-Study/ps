인접리스트 구현이 처음에 기억이 안 남, 실행 몇번 해보다가 풀음
graph[a].append(b)는 기억이 났다. []가 n+1개 있는 2차원 리스트여야 하니까 초기화를 해냈다.
1번노드~n번노드니까 visited, graph n+1개 

완전탐색 위해 visited[i] = True, False 붙이는 곳 그냥 다 붙였다 - 찍어서 푼 느낌
dfs안에 있는 처음 visited는 필요없는듯 근데 중복돼도 문제는 없었다. 나머지는 완탐위해 모두 필요
1번 노드부터 탐색시작 하고나서 다시 2번부터 탐색시작할때 1번이 false여야 하니 방문하고 false
안 이어진 노드 모두 탐색해보기 위해 1~n 노드 모두 각각 시작으로 탐색해본다.
1번노드 시작 탐색 안에서 갈래


T = int(input())
def dfs(x, cnt):
    global max_cnt
    cnt += 1
    max_cnt = max(max_cnt, cnt)
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt)
            visited[i] = False

            
for tc in range(1, T+1):
    n, m = map(int, input().split())
    answer = 1
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    max_cnt = 0
    for i in range(1, n + 1):
        visited[i] = True
        dfs(i, 0)
        visited[i] = False

                
    print("#{} {}".format(tc, max_cnt))
