from collections import deque


def solution(bridge_length, weight, truck_weights):
    sec = 0
    q = deque([])
    tr = deque(truck_weights)
    q_sum = 0

    while tr:
        sec += 1
        while q and sec - q[0][1] == bridge_length:
            #초당 1 이동하니까 현재 초를 기준으로 건너간 거리 계산 후 pop
            tmp = q.popleft()
            q_sum -= tmp[0]

        cur_tr = tr[0]
        if q:
            if q_sum + cur_tr <= weight:
                q_sum += cur_tr
                q.append([tr.popleft(), sec])
                # 초를 사용해 지나간 거리 계산해야하므로 덱에 들어갈때 sec도 같이 삽입

        else:
            q_sum += cur_tr
            q.append([tr.popleft(), sec])

    while q:
        # 덱에 남아있는 거 연산
        sec += 1
        if sec - q[0][1] == bridge_length:
            tmp = q.popleft()

    return sec