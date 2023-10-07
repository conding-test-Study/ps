# 다시 풀이하여 정답 획득
def solution(n, computers):
    visited = [False] * n

    def dfs(x):

        for i in range(n):
            if i != x and computers[x][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)

    # dfs 1묶음 실행마다 cnt += 1 실행
    # computers 리스트의 인덱스는 0 ~ n-1 까지 있다고 생각하기
    cnt = 0
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(j)
            cnt += 1

    return cnt
