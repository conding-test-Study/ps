import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
room = []

for i in range(n):
    s, e = map(int,input().split())
    room.append([s,e])

room.sort() # 시작시간 기준으로 정렬
q = []
heappush(q, room[0][1])

for i in range(1, n):
    if q[0] <= room[i][0]:
        # 새로운 강의의 시작시간이 우선순위큐 맨 앞의 강의의 종료시간보다 늦거나 같으면 우선순위 큐 맨 팝하고 푸쉬
        print(heappop(q))

    # 새로운 강의의 시작시간이 우선순위큐 맨 앞의 강의의 종료시간보다 빠르면 바로 힙푸쉬
    heappush(q, room[i][1])

print(len(q)) # 우선순위큐 길이가 필요한 강의실 갯수

# 회의실배정이랑 비슷한 문제인가? 하고 비슷하게 접근했다가 당해버린 문제
# 회의실배정은 회의실이 하나로 고정되어있는 상황이라 종료시간을 기준으로 정렬해서 쉽게 풀리지만
# 이 문제는 여러개의 강의실이 존재할 수도 있기 때문에 종료시간으로 정렬해서 간편하게 풀 수 없는 문제이다.
# 우선순위큐를 이용해 푸는 것까진 대충 접근했으나 로직을 떠올리지 못해 답을 찾아보았다.

