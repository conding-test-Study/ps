def solution(brown, yellow):
    answer = []

    if yellow == 1:
        answer.append(yellow+2)
        answer.append(yellow+2)

    elif yellow > 1:

        for i in range(1, yellow // 2 + 1):

            # i는 세로, j는 가로

            if yellow % i == 0:
                j = yellow // i

                # 각 꼭대기 4 + 세로*2 + 가로*2 == brown 이면
                # 주어진 요건 충족하는 사각형 제작 가능
                # 사각형 제작 이후 가로+2, 세로+2 answer에 저장
                if 4 + i*2 + j*2 == brown:
                    answer.append(j+2)
                    answer.append(i+2)
                    break

    return answer
