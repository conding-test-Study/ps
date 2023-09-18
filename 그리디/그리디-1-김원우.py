import sys
input = sys.stdin.readline

n = int(input())
room = []

for i in range(n):
    start, end = map(int,input().split())
    room.append([end, start])

room.sort() # 회의 종료 시간 기준으로 정렬
cnt = 0
prev_start = 0
prev_end = 0

for time in room:
    new_start = time[1]
    new_end = time[0]

    if new_start >= prev_end: # 새로 꺼낸 회의실 시작 시간이 이전 회의의 끝나는 시간보다 크거나 같으면
        cnt += 1
        prev_end = new_end

print(cnt)

