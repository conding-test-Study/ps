import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
room = []

for i in range(n):
    s, e = map(int,input().split())
    room.append([s,e])

room.sort()
q = []
heappush(q, room[0][1])

for i in range(1, n):
    if q[0] <= room[i][0]:
        heappop(q)

    heappush(q, room[i][1])

print(len(q))


