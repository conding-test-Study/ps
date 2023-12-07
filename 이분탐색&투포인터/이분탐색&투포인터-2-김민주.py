# 1의 갯수를 dp[1]에 저장한다는 발상 자체는 맞았는데, 코드가 지저분해지면서 오류 발생
# 원래 쓴 코드


import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 같은 정수 K개 이하 포함하는 부분수열?


def count_nums(li):
    dp = [0 for _ in range(10**6 + 1)]

    for k in range(K+1):
        d = li[k]
        dp[d] += 1

    start = 0
    end = start + K
    max_dp = max(dp)

    while True:
        if max_dp <= K:
            end += 1
            dp[li[end]] += 1
            if dp[li[end]] == max_dp + 1:
                max_dp += 1
            print(li[start:end])
        # elif max(dp) > K and dp[li[start]] == max(dp):
        elif max_dp > K and dp[li[start]] == max_dp:
            dp[li[start]] -= 1
            max_dp -= 1
            start += 1
            dp[li[start]] += 1
            print(li[start:end])
        # elif max(dp) > K and dp[li[end]] == max(dp):
        elif max_dp > K and dp[li[end]] == max_dp:
            print(li[start:end])
            break
        else:
            break

    print(start, end)
    print(end - start)


count_nums(nums)


# 예시 답안 코드 (출처: https://kimmeh1.tistory.com/474)
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
