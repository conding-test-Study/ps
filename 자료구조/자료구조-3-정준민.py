import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

for i in range(N):
    # 큐가 비어있지 않고 이전 최소값이 구간을 벗어난 경우 pop
    if q and q[0][0] <= i - L:
        q.popleft()

    # 새로 들어온 값보다 큰 수들은 전부 pop
    while q and arr[i] < q[-1][1]:
        q.pop()

    # 큐에 (인덱스, 값) 삽입
    q.append((i, arr[i]))

    # 큐의 가장 왼쪽 값이 현재 구간에서의 최소값이 됨
    print(q[0][1], end=' ')
