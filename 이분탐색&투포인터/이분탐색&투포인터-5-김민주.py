import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]

# lines 각 원소 하나하나를 start, end로 삼아서 그 안에 dots가 몇 개 있는지 판단하는 거로 하기
# dots 탐색횟수를 줄일 방법은?

dots.sort()


def count_dots(start, end):
    cnt = 0
    # 과연 전체탐색을 꼭 해야하는가?
    for dot in dots:
        if start <= dot <= end:
            cnt += 1
        elif dot > end:
            break

    return cnt


for line in lines:
    a, b = line[0], line[1]
    print(count_dots(a, b))

# 이분탐색 적용한 예시코드 가져오기 (출처: https://jjini-3-coding.tistory.com/14)

n, m = map(int, sys.stdin.readline().split())
dot = list(map(int, sys.stdin.readline().split()))
dot.sort()


def dot_min(a):  # 선분 중 가장 작은 점 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):   # 선분 중 가장 큰 점 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1)
