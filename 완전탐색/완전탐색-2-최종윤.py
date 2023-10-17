# 처음에 그리디? 같이 아무것도 없는 맵에 가장 작은 값 갖는 위치 차례대로 한 개씩 골랐지만 틀렸다 .
# 가장작은거 를 순서대로 2개 뽑는 것보다 두개를 합쳐서 더 작은 경우가 있을 수 있기 때문인가보다 
# 1번문제도 비슷한 이유로 그리디로 풀면 안 되는 문제였는데


from itertools import combinations
import sys
input = sys.stdin.readline

def check(li):
    global answer
    visited = [[False]*n for i in range(n)]
    total = 0

    for r,c in li:
        visited[r][c] = True
        total += arr[r][c]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not visited[nr][nc]:
                visited[nr][nc] = True
                total += arr[nr][nc]
            else:
                return
    answer = min(answer, total)
        




dr = [-1,1,0,0]
dc = [0,0,-1,1]

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
answer = sys.maxsize
loc = []
for i in range(1,n-1):
    for j in range(1,n-1):
        loc.append([i,j])

for li in combinations(loc, 3):
    check(li)
print(answer)
