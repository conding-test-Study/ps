# 답안 ('틀렸습니다' 판정)
# 틀린 이유를 찾기 어려워서 코드 리뷰 예정, 혹은 시간을 두고 고쳐나갈 계획

import sys
from collections import deque

T = int(input())
i = 0

while i <= T-1:
    P = sys.stdin.readline()
    n = int(sys.stdin.readline())
    X = eval(sys.stdin.readline())

    D = deque(X)

    r_count = 0

    for p in P:
        if p == 'D':
            if n > 0:
                if r_count % 2 == 0:
                    D.popleft()
                    n -= 1
                elif r_count % 2 == 1:
                    D.pop()
                    n -= 1
            elif n == 0:
                print("error")
                break
        elif p == 'R':
            r_count += 1

    if r_count % 2 == 1:
        D.reverse()

    if n != 0:
        print(list(D))

    i += 1
