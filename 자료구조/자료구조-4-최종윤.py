# 힙에 대해 아는 것이 없어 찾아보고 풀었다. 시간 초과가 나서 input을 sys로 수정했다.

import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            k = heapq.heappop(heap)[1]
            print(k)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
 
