# 입력된 리스트를 덱으로 만들고, 원소를 하나씩 뽑아서 순회시키는 구성

from collections import deque


def solution(prices):
    answer = []

    P = deque(prices)

    while P:
        price = P.popleft()
        count = 0

        for p in P:
            if price > p:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


print(solution([1, 2, 3, 2, 3]))
