# solved가 들어왔을때 힙 안의 문제를 어떻게 처리할지 생각하다가 막혀서 답 찾아봄
# 딕셔너리를 통해 해결할 수 있다는걸 알게됨.

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
minH, maxH = [],[]
d = {}

for i in range(n):
    P,L = map(int, input().split())
    heappush(minH, [L,P])
    heappush(maxH, [-L,-P])
    d[P] = True

m = int(input())
for i in range(m):
    command = input().split()
    if command[0] == "recommend":
        if command[1] == '1':
            while not d[-maxH[0][1]]:
                heappop(maxH)
            print(-maxH[0][1])
        elif command[1] == '-1':
            while not d[minH[0][1]]:
                heappop(minH)
            print(minH[0][1])
    elif command[0] == "add":
        P, L = int(command[1]), int(command[2])

        while not d[-maxH[0][1]]:
            heappop(maxH)
        while not d[minH[0][1]]:
            heappop(minH)
        d[P] = True
        heappush(minH, [L,P])
        heappush(maxH, [-L,-P])
    else:
        d[int(command[1])] = False
