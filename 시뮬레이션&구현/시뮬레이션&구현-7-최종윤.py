#인접행렬에 대해서 본적있어서  그냥 풀린건가 ,  2차원 배열이랑 크게 다르지 않은것 같네
#연결요소 개수 구하는것도 풀었었고 

def solution(n, computers):
    answer = 0
    visited = [False] * n 
    #존재하는 모든 노드에 대해 한 번씩 dfs 돌린다.   인접하지 않은 노드를 위해 
    # dfs 할때마다 answer += 1
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers, visited)
    
    return answer

def dfs(node, computers, visited):
    #방문 안 한, 연결된, 인접한 노드를 모두 방문한다
    for i in range(len(computers)):
        if computers[node][i] == 1:
            if not visited[i]:
                visited[i] = True
                dfs(i, computers, visited)
