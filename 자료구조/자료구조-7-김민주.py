from collections import deque


def solution(bridge_length, weight, truck_weights):

    # 다리를 0이 bridge_length만큼 있는 deque으로 표현
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)

    # 아래 phase 한 파트가 1초이고, phase 갯수를 answer 변수에 저장
    answer = 0

    # 트럭 무게 변수를 별개로 저장. sum 사용 시 시간초과 발생.
    total_weights = 0

    # 트럭을 전부 다리 위로 보낼 때까지의 전개
    while trucks:
        b = bridge.popleft()
        total_weights -= b

        truck = trucks[0]

        if total_weights + truck > weight:
            bridge.append(0)
            print(bridge)
            answer += 1
        else:
            bridge.append(truck)
            total_weights += trucks.popleft()
            print(bridge)
            answer += 1

    # trucks 덱에서 원소가 다 빠진 뒤
    # bridge 덱을 다리 길이 전체에 0만 있는 형태로 만들기
    while True:
        if bridge == deque([0 for _ in range(bridge_length)]):
            break

        else:
            bridge.popleft()
            bridge.append(0)
            print(bridge)
            answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
