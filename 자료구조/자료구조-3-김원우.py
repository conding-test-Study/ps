import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int,input().split())
arr = list(map(int,input().split()))
D = []
q = deque([])

for i in range(N):
    # 덱이 비어있지 않고 덱의 맨 뒤가 추가하려는 원소보다 크면 제거 (덱을 오름차순으로 유지하기 위함)
    while q and q[-1][0] > arr[i]:
        q.pop()
    q.append([arr[i], i])
    # 덱의 맨 앞 원소의 인덱스가 슬라이딩 윈도우를 벗어났으면 제거
    if q[-1][1] - q[0][1] == L:
        q.popleft()
    D.append(q[0][0]) # 덱의 맨 앞은 항상 슬라이딩 윈도우 내 최솟값
print(*D)