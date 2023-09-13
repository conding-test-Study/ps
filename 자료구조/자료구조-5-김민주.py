# 문제에서 주어진 명령어가 recommend만 있었다면 스택, 큐 + 정렬 로 풀어도 되지만, add와 solved를 풀 방법이 없어짐.
# 이하 아이디어는 recommend -1을 최소 힙, recommend 1을 최대 힙으로 풀이함 (참고: https://sinawi.tistory.com/m/502)
# add : 최소 힙, 최대 힙에 원소 집어넣기
# solved : 최소 힙, 최대 힙에서 원소 제거하기
# 같은 번호인데 제거-첨가를 거치면서 난이도가 바뀌는 경우를 체크하기 위해 level 딕셔너리 이용

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

# (10000, 5) 형태 입력
N = int(input())
min_h = []
max_h = []
level = {}

for n in range(N):
    P, L = map(int, input().split())
    heappush(min_h, (L, P))
    heappush(max_h, (-L, -P))
    if not level.get(P):
        level[P] = 0
    # level의 원소는 {문제번호: 난이도} 이렇게 기록됨
    level[P] = L

# recommend -1, add 1000 48 등 형태로 입력
M = int(input())
for m in range(M):
    c, *args = input().split()

    if c == 'add':
        P, L = map(int, args)
        heappush(min_h, (L, P))
        heappush(max_h, (-L, -P))
        if not level.get(P):
            level[P] = 0
        level[P] = L

    # solved의 경우, level 딕셔너리에서 문제 난이도에 해당하는 영역을 0으로 만들어버림
    elif c == 'solved':
        P = int(args[0])
        level[P] = 0

    else:
        # recommend 파트
        x = args[0]
        if x == '1':  # 최대힙 활용

            # 최대힙의 해당 문제 & 난이도가 사실 level 딕셔너리에서는 이미 없어진 것일 경우, 최대힙 정리하기
            # 정리 이후 최대힙에서 문제 번호 뽑아내기
            while max_h and level[-max_h[0][1]] != -max_h[0][0]:
                heappop(max_h)
            print(-max_h[0][1])

        else:   # 최소힙 활용

            # 최소힙의 해당 문제 & 난이도가 사실 level 딕셔너리에서는 이미 없어진 것일 경우, 최소힙 정리하기
            # 정리 이후 최소힙에서 문제 번호 뽑아내기
            while min_h and level[min_h[0][1]] != min_h[0][0]:
                heappop(min_h)
            print(min_h[0][1])
