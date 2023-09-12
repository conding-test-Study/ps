# 내 답안 (시간초과)
# 이중 for문을 이용하여, 각 주인이 볼 수 있는 건물의 수를 직접 구함

from collections import deque
import sys

N = int(sys.stdin.readline())
H = [int(sys.stdin.readline()) for _ in range(N)]

D = deque()

answer = 0

for n in range(N):
    D.append(H[n])

    for i in range(n+1, N):
        if H[i] < D[-1]:
            answer += 1
        else:
            break

print("정답: ", answer)

# 모범 답안 (참고: https://lakelouise.tistory.com/62 외 다수)
# 각 건물별로 볼 수 있는 사람의 수를 더한다는 발상
# '각 건물별로 볼 수 있는 사람의 수'를, 스택[-1] 원소와 현재 해당 원소를 비교하여 스택에 넣고 뺀 뒤 그 스택의 갯수를 세서 측정하기
n = int(input())

arr = [int(input()) for i in range(n)]
stk = []
ans = 0

for i in range(n):
    while stk and stk[-1] <= arr[i]:
        stk.pop()

    stk.append(arr[i])
    ans += len(stk) - 1

print(ans)
