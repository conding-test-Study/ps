from collections import deque


def solution(bridge_length, weight, truck_weights):
    sec = 0
    q = deque([])
    tr = deque(truck_weights)
    q_sum = 0

    while tr:
        sec += 1
        while q and sec - q[0][1] == bridge_length:
            tmp = q.popleft()
            q_sum -= tmp[0]

        cur_tr = tr[0]
        if q:
            if q_sum + cur_tr <= weight:
                q_sum += cur_tr
                q.append([tr.popleft(), sec])

        else:
            q_sum += cur_tr
            q.append([tr.popleft(), sec])

    while q:
        sec += 1

        if sec - q[0][1] == bridge_length:
            tmp = q.popleft()

    return sec