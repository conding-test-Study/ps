import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 반례
# input:
# 3
# 1000 1
# 2000 37
# 3000 55
# 4
# solved 2000
# add 2000 70
# solved 1000
# recommend -1
#
# output:
# 2000
# 정답:3000
# 중간에 껴있는 문제 삭제-> 방금 삭제한 번호의 문제 다시 추가의 경우
# 처음 삭제된 문제가 맨 앞으로 오면 삭제가 안된걸로 체크

N = int(input())
mx_heap = []
mn_heap = []
chk = [False for _ in range(100001)]
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(mx_heap, (-L, -P))
    heapq.heappush(mn_heap, (L, P))
    chk[P] = True

M = int(input())
for _ in range(M):
    tmp = input().split()
    if tmp[0] == 'add':
        heapq.heappush(mx_heap, (-int(tmp[2]), -int(tmp[1])))
        heapq.heappush(mn_heap, (int(tmp[2]), int(tmp[1])))
        chk[int(tmp[1])] = True
    elif tmp[0] == 'recommend':
        if tmp[1] == '-1':
            while not chk[mn_heap[0][1]]:
                heapq.heappop(mn_heap)
            print(mn_heap[0][1])
        else:
            while not chk[-mx_heap[0][1]]:
                print(heapq.heappop(mx_heap))
            print(-mx_heap[0][1])
    else:   # solve
        chk[int(tmp[1])] = False
        while not chk[mn_heap[0][1]]:
            heapq.heappop(mn_heap)
        while not chk[-mx_heap[0][1]]:
            print(heapq.heappop(mx_heap))