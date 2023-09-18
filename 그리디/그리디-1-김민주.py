# 첫 풀이 (시간 초과)
# 문제 내용을 그대로 코드로 구현하는 데에 집중
# 이중 for문을 돌리면서 시간 초과가 발생한 것으로 추정

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
meets = sorted([tuple(map(int, input().split())) for _ in range(N)])

print(meets)

table = deque()
counts = deque()
count = 0

for i in range(N):
    table.append(meets[i])
    count += 1

    for j in range(i+1, N):
        if meets[j][0] >= table[-1][1]:
            table.append(meets[j])
            count += 1

    print("시간표: ", table)
    if counts:
        if counts[-1] <= count:
            counts.append(count)
    else:
        counts.append(count)

    count = 0
    table.clear()

print(counts[-1])


# 모범 풀이 (출처: https://hongcoding.tistory.com/22)
# 회의실 사용 회의 수를 늘리려면: 먼저 시작하고 빨리 끝나서, 다음 회의를 빠르게 채울 수 있도록 해야 함
# 이 논리에 따라 시작 시간 기준 정렬 + 이를 기반으로 종료 시간 기준 정렬 -> 이후 회의의 갯수 cnt로 측정
# 리스트 순회 횟수를 최소화할 수 있다는 점에서 시간 복잡도 줄이는 데에 유리
n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key=lambda x: x[0])
room.sort(key=lambda x: x[1])
print(room)

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)
