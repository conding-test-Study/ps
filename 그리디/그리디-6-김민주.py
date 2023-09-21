# 리스트 및 정렬을 통해 '지금 회의중' 리스트를 기준으로 비교하며 방 갯수를 구하려고 함
# 여러 반례에 대한 답을 찾았으나 지속적으로 오답 처리됨

import heapq
import sys

input = sys.stdin.readline


N = int(input())
meets = [tuple(map(int, input().split())) for _ in range(N)]

meets.sort(key=lambda x: x[0])
print(meets)

rooms = 0
meeting = []

for i in range(N):
    if meets[i][0] < meets[i-1][1]:
        if meeting:
            for meet in meeting:
                if meets[i][0] >= meet[1]:
                    meeting.remove(meet)
                    meeting.append(meets[i])
                    print("지금 회의중: ", meeting)
                    break
                else:
                    meeting.append(meets[i])
                    rooms += 1
                    print("지금 회의중: ", meeting)
                    break

        else:
            meeting.append(meets[i])
            rooms += 1
            print("지금 회의중: ", meeting)


print(rooms)

# 모범 아이디어: 리스트 + 최소 힙 이용 (출처: https://junbangg.github.io/boj/19598/)
# '지금 회의중'을 힙으로 처리.
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(N)])
h = []
for start, end in schedules:
    if h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)

print(len(h))
