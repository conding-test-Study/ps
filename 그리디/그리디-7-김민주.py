# 문제 아이디어를 코드로 구현하는 것이 어려워 답을 찾지 못함
# 이하 답안 코드 (출처: https://hillier.tistory.com/105)

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])

box = [C]*(N+1)  # [40, 40, 40, 40, 40] 식으로 트럭 최대 적재량으로 이루어진 리스트 생성
print(box)
answer = 0
for s, e, b in arr:
    _min = C
    for i in range(s, e):
        _min = min(_min, box[i])
    _min = min(_min, b)
    for i in range(s, e):
        box[i] -= _min
    answer += _min

print(answer)
