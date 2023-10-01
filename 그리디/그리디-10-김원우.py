def solution(n, lost, reserve):
    reserve.sort()

    for i in range(len(reserve)):
        # 여분 체육복 있는 놈도 도난 당했을 수 있음
        # 여분 있는 애들 중 도난 당한애들 있으면 배제
        if reserve[i] in lost:
            idx = lost.index(reserve[i])
            del lost[idx]
            reserve[i] = 1000000

    for i in range(len(reserve)):
        # 여분 가지고 있는 놈들 번호 기준 앞뒤 친구들 잃어버린 목록에 있는지 체크 후 배열에서 삭제
        if reserve[i] - 1 in lost:
            idx = lost.index(reserve[i] - 1)
            del lost[idx]

        elif reserve[i] + 1 in lost:
            idx = lost.index(reserve[i] + 1)
            del lost[idx]
    print(lost)
    return n - len(lost)