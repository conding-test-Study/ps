import sys
import heapq
input = sys.stdin.readline

#정렬한다. o

#회의 끝나는 시간 보다 먼저 시작해버리면 새 회의실 쓴다. 가장빨리끝나는것보다

#진행중인회의 끝나는 시간 담겨있는 end

#있는 회의 끝나고 하는거면 heappop하고 hpush

#새로 회의실 쓰면 heappush



n = int(input())

c = []
for i in range(n):
    c.append(list(map(int,input().split())))

c.sort()

end = []   
end.append(c[0][1])

for i in range(1, n):
    if c[i][1] < end[0]:
        heapq.heappush(end, c[i][1])
    else:
        heapq.heappop(end)
        heapq.heappush(end, c[i][1])


print(len(end))
