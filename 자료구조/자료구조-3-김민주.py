# 첫 풀이 (시간 초과)
# 많은 코딩테스트 문제가 그렇듯 문제에 써 있는 대로 코드를 짜면 무조건 시간초과 발생
# 그래서 '같은 상황을 설명하는 다른 논리'를 고안해야 하고 그 방식이 자료구조 활용

import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

D = []
result = []

for n in range(N):
    if n < L:
        # A1부터 An까지 중 최소값 고르기
        # 일단 A1부터 An까지 집어넣고, 집어넣는 과정에서 최소값 고르기
        D.append(A[n])
        result.append(min(D))
    else:
        D.append(A[n])
        del D[0]
        result.append(min(D))

print(*result)

# 정답 코드 분석
input = sys.stdin.readline
N, L = map(int, input().split())
num = list(map(int, input().split()))

# 최솟값을 구할 곳. 덱에 적히는 값은 (0, 3) 과 같은 형태
# 덱에는 슬라이딩 윈도우의 범위를 넣음. 단, '최소값 후보'에 가까울수록 덱 왼쪽에 놓일 수 있도록 함
temp = deque([])

for i in range(N):
    # 덱에 원소가 있고, 그 원소의 인덱스가 i-L보다 작으면 덱에서 제거
    if temp and temp[0][0] <= i-L:
        temp.popleft()

    # 덱에 원소가 있고, 새로 들어올 원소가 덱의 마지막 원소보다 작으면 기존 원소 삭제
    while len(temp) >= 1 and num[i] < temp[-1][1]:
        temp.pop()

    # 덱에 새 원소 넣기
    temp.append((i, num[i]))

    # 덱 첫번째 원소의 해당 값이 해당 슬라이딩 윈도우의 최소값
    print(temp[0][1], end=" ")
