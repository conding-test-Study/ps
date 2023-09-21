# 정답참고함

import sys

input = sys.stdin.readline
n, space = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
send = []
answer = 0

for i in range(m):
    a, b, amount = map(int, input().split())
    send.append([a, b, amount])
send.sort(key=lambda x: (x[1], x[0]))

for start, destination, boxes in send:
    maxbox = boxes

    for i in range(start, destination):
        maxbox = min(maxbox, space - box[i])

    for i in range(start, destination):
        box[i] += maxbox
    answer += maxbox
print(answer)