# 답 찾아봄
# 투포인터 범위 잡아주는거 헷갈렸는데 답보면서 이해함

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0

counter = [0] * (max(numbers) + 1)
answer = 0
while right < N:
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        right += 1
    else:
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)