from collections import deque


def solution(priorities, location):
    origins = deque()
    i = 0

    # origins deque에 (1, 0) 형태로 원소와 인덱스를 튜플로 넣기
    for p in priorities:
        origins.append((p, i))
        i += 1

    print(origins)

    results = []

    # origins 덱에서 첫 원소를 떼네어 그 다음부터의 원소와 크기 비교
    # 떼어진 첫 원소보다 큰 원소가 없으면 results에 넣고, 그렇지 않으면 덱 맨 뒤로 넘기기
    while origins:
        o1 = origins.popleft()

        b = 0
        for o in origins:
            if o1[0] < o[0]:
                origins.append(o1)
                b += 1
                break
            else:
                pass

        print("큐: ", origins)

        if b == 0:
            results.append(o1)

        print("실행 목록: ", results)

    # 원하는 원소 인덱스 찾기
    answer = 0
    for r in results:
        if r[1] == location:
            answer = results.index(r) + 1

    return answer


print("정답: ", solution([1, 1, 9, 1, 1, 1], 0))
