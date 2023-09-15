# 힙 활용
# heappop 2개 하기 -> 2개 조합의 스코빌 지수가 K보다 작으면 합을 heappush, 합이 K보다 크면 거기서 stop
# 일부 테스트 케이스 오답 발생

from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)

    answer = 0

    while len(scoville) >= 2:

        most_hot = heappop(scoville)
        most_hot2 = heappop(scoville)

        if most_hot >= K:
            break
        else:
            score = most_hot + 2 * most_hot2

            if score >= K:
                heappush(scoville, score)
                answer += 1
                break
            else:
                heappush(scoville, score)
                answer += 1

    if heappop(scoville) < K:
        answer = -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))


# 모범 답안 참고 이후 수정 (참고: https://velog.io/@younge/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%94-%EB%A7%B5%EA%B2%8C-%ED%9E%99)


def solution(scoville, K):
    heapify(scoville)

    answer = 0
    # 리스트의 최솟값이 K보다 작은 경우
    while scoville[0] < K:

        # heappop 2번을 해주기 위해 len(scoville) > 1 조건 추가
        # len(scoville) > 1 조건 안 맞으면 함수 멈추기
        if len(scoville) > 1:
            score = heappop(scoville) + 2 * heappop(scoville)
            answer += 1
            heappush(scoville, score)

            if len(scoville) == 1 and scoville[0] < K:
                answer = -1

        else:
            break

    return answer
