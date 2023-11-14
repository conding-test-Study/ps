#dp
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cache = [1] * N
    for i in range(N):
        for j in range(i):
            if data[i] > data[j]:
                cache[i] = max(cache[j] + 1, cache[i])


 
    print("#{} {}".format(tc, max(cache)))
#binary search
from bisect import bisect_left
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cache = [1]
    x = [data[0]]
    for i in range(1, N):
        if data[i] > x[-1]:
            x.append(data[i])
            cache.append(cache[-1] + 1)
        else:
            idx = bisect_left(x, data[i])
            x[idx] = data[i]


 
    print("#{} {}".format(tc, max(cache)))


