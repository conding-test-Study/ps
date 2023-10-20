# permutations로 dungeons 나열 가능한 경우의 수 전부 만들고
# 그 경우의 수 중 진입 가능한 곳이 가장 많은 경우를 찾기

from itertools import permutations


def count_number(std, lis):
    cnt = 0

    for li in lis:
        a, b = li[0], li[1]
        if std < a:
            break
        else:
            std -= b
            cnt += 1

    return cnt


def solution(k, dungeons):

    li = permutations(dungeons)
    result = []

    for l in li:
        r = count_number(k, l)
        result.append(r)

    answer = max(result)
    return answer
