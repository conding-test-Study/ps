import sys

input = sys.stdin.readline

N, X = map(int, input().split())

people = list(map(int, input().split()))

# 2일 동안 가장 많이 들어온 방문자수 찾기: start, end 찍어서 투포인터로 찾기


def most_visited(li):
    result = []

    r = 0
    for s in range(X):
        r += li[s]
    result.append(r)

    # 부분합 구하기: li[0] ~ li[X-1] 구하고,
    # 그 이후 리스트 탐색하면서 기존 li[start]를 빼고, 새 li[end]를 더해주기
    for start in range(1, N):
        end = start + X - 1
        if end >= N:
            break

        else:
            rs = result[-1] - li[start-1] + li[end]
            result.append(rs)

    return result


res = most_visited(people)
print(res)

ans = max(res)

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(res.count(ans))
