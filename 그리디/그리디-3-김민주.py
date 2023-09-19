# 처음 코드 (예시 늘리자 IndexError 발생)
# 그리디 1번 문제의 발상을 그대로 가져오되, 해당 문제의 '리스트 1바퀴 순회'를 '강의실 1개'로 집계

import heapq
import sys

input = sys.stdin.readline

N = int(input())
lessons = [tuple(map(int, input().split())) for _ in range(N)]

lessons.sort(key=lambda x: x[0])
lessons.sort(key=lambda x: x[1])

print(lessons)

rooms = 0

while len(lessons) > 1:
    end = lessons[0]
    print("현재: ", lessons)
    print("시작점: ", end)

    for i in range(1, len(lessons)):

        if lessons[i][0] >= end[1]:
            now = lessons[i]
            lessons.remove(end)
            end = now

            if i == len(lessons):
                lessons.remove(end)

    rooms += 1
    print("교실수: ", rooms)

print("남은 수업: ", lessons)

if len(lessons) > 0:
    rooms += 1

print(rooms)

# 해당 코드는 오류도 있었으나, 기본적으로 리스트를 여러 회 순회한다는 점에서 시간 복잡도 문제 발생
# 모범 코드의 경우 최소 힙 활용 (출처: https://hongcoding.tistory.com/79)
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:  # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1])  # 새로운 회의실 개설
    else:
        # 현재 회의실에 이어서 회의 개최 가능
        # 원소 제거 후 추가 진행되기 때문에 힙 전체의 원소 갯수 불변
        heapq.heappop(room)  # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))
