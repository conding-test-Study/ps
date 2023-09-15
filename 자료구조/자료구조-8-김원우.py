from collections import deque

def solution(priorities, location):
    answer = 0

    p = deque([])
    cnt = 0

    for i in range(len(priorities)):
        p.append([priorities[i], i])
        # location 처리를 위해 인덱스랑 같이 저장
    while p:
        tmp = p.popleft()
        if not p:
            # 현재 뽑은 프로세스가 마지막 프로세스였다면
            answer = len(priorities)
            break
        m = max(p)

        if tmp[0] >= m[0]:
            cnt += 1
            idx = tmp[1]

            if idx == location:
                answer = cnt
                break
        else:
            p.append(tmp)
    return answer