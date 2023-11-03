def solution(n):
    cache = [0 for _ in range(10**6 + 1)]

    cache[0] = 0
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]

    answer = cache[n]
    return answer % 1234567
