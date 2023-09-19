import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 올해는 4, 6, 9, 11월은 30일까지 있고,
# 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며,
# 2월은 28일까지만 있다.

# 1. 정렬
# 2. 큐가 비어있음 -> 3월1일 이전에 피는 꽃들 중 더 늦게까지 피어있는 꽃을 골라서 담음
# 3. 큐가 비어있지 않음 -> 마지막으로 담겨있는 꽃이 지는 날짜와 같거나 큰 날짜를 골라서 담음
#                   -> 만약 큐의 길이가 2 이상이고, 전 전 꽃이 지는 날짜와 같거나 큰 날짜 중 전 꽃보다 더 오래 펴있으면 바꿈
date = []
n = int(input())
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    date.append([[sm, sd], [em, ed]])

date.sort(key=lambda x:x[0])
date.sort(key=lambda x:x[1])
for v in date: print(v)
q = deque()
q.append(date[0])
for i in range(1, n):
    # 맨 처음 꽃
    if date[i][0][0] <= 2 and (q[0][1][0] < date[i][1][0] or (q[0][1][0] == date[i][1][0] and q[0][1][1] < date[i][1][0])):
        q.popleft()
        q.append(date[i])
    else:
        if q[-1][1][0] < date[i][1][0] or (q[-1][1][0] == date[i][1][0] and q[-1][1][1] < date[i][1][0]):




print(q)
