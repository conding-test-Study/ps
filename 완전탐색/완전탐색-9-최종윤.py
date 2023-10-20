#답지확인
#최소 최대 나오면 그리디가 떠올랐음 그러나 몇번 푸니까 확인을 해봐야하는구나 그래서
#모든 가능한 경우를 모두 비교해서 최대값을 구하는 dfs 완전탐색방식 또는 조합?그런것들을
#이용한 풀이가 나올 수 있겠다 생각했음 완전탐색 문제인걸 알고 있으니까..

#[1]이 작은 것부터 고르면 [0] 이 큰 것중에 사용하고나서 [1]이 작은것을 하면 더 많이 할 수 있는데 
#[1]작은 것부터 하다가 [0]최소 피로도 넘어가버리면 더 못한 결과가 나올 수 있음
#[0]이 큰 것 중에 [1]을 작은것을 골라도 최대값 보장 못함


#그러나 완전탐색 방식풀이를 떠올리지 못하겠다 
#dfs를 어떤 순서로 방문해야하는가? 맞다 그냥 인접한 노드다 방문하도록하는데 그냥 무작위로 상하좌우했었지
#여기서는 그냥 0번 던전부터 n번 던전까지 방문하는데 visited를 1했다가 dfs ->v = 0해서 완전탐색 모든경우의수
#dfs는 종료조건이 있던데 n번째 던전에 도달하지 못하고 남은 k가 소모피로도보다 크지 못하면 끝나겠네
#그냥 모든 cnt랑 비교하고 max값을 찾는다?
#k는 하나의 값을 공유하는게 아니라 탐색 경우의 수마다 다른 k값을 가져야하니 dfs를 돌면서 값을 주도록
#parameter로 설정해야겠다. cnt도 동일하게
#방문배열도 탐색 경우의수마다 달라지겠구나 parameter로 줘야겠구나


answer = 0
def DFS(k, cnt, dungeons, ch):
    global answer
    answer = max(answer, cnt)
    # recursion call
    for i in range(len(dungeons)):
        if ch[i] == 0 and k >= dungeons[i][0]:
            ch[i] = 1
            DFS(k-dungeons[i][1], cnt+1, dungeons, ch)
            # close one cycle i -> reset ch[]
            ch[i] = 0

def solution(k, dungeons):
    ch = [0]*len(dungeons)
    # first call fisrt state
    DFS(k, 0, dungeons, ch)
    return answer
