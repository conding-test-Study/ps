#답지확인

#첫풀이
import sys

input = sys.stdin.readline

stk = [[]]
n = int(input())
tmp = []
for i in range(n):
    tmp.append(list(map(int,input().split())))
tmp.sort()


e = 0
j = 0
for i in range(n):
    if e <= tmp[i][0]:
        stk[j].append(tmp[i])
        e = tmp[i][1]
    else:
        # 지금 stk에 들어갈수 없으면 반복
        while j < len(stk) and stk[j][-1][1] > tmp[i][0]:
            j += 1

        # 들어가는 경우
        if j < len(stk) and stk[j][-1][1] <= tmp[i][0]:
            stk[j].append(tmp[i])

        #추가된 강의실에 모두 들어갈 수 없으면 강의실 추가
        if j == len(stk):
            stk.append([tmp[i]])
            
        
            
        e = tmp[i][1]
        j = 0

print(len(stk))



#여러개에서 작은거 뽑는데 들어갔다 나갔다 할 때 정렬하는것보다 우선순위 큐가?
        #종료시간 빠른 회의실부터 회의 개최해야함
        #근데 0번회의부터 그냥 들어갈 수 있는 경우라면 먼저 들어가버려서 그런

import sys
import heapq

input = sys.stdin.readline

stk = []
n = int(input())

c = []
for i in range(n):
    c.append(list(map(int,input().split())))
c.sort()


heapq.heappush(stk, c[0][1])

for i in range(n):
    
#새로운 강의실 사용 (더 빨리 시작할 때 빨리 끝나는것보다)
    if c[i][0] < stk[0]:
        heapq.heappush(stk, c[i][1])
#기존 강의실 사용해서 빨리 끝나는거 빼고 거기에서 하도록
    else:
        heapq.heappop(stk)
        heapq.heappush(stk, c[i][1])            
        
print(len(stk))
