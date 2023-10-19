# DFS 백트래킹문제.
# 설계 중 실수만 안하면 간단한 문제

def solution(k, dungeons):
    answer = -1

    def dfs(visited, cnt, k):
        nonlocal answer
        answer = max(answer, cnt)
        for idx, d in enumerate(dungeons):
            if visited[idx] == 0 and k >= d[0]:  # 방문 안했고 피로도 가능할때
                visited[idx] = 1
                dfs(visited, cnt + 1, k - d[1])
                visited[idx] = 0

    for i in range(len(dungeons)):
        visited = [0] * len(dungeons)
        if dungeons[i][0] <= k:
            visited[i] = 1
            dfs(visited, 1, k - dungeons[i][1])
    return answer