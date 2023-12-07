# 출처: https://velog.io/@younge/Python-프로그래머스-정수-삼각형-동적계획법
# triangle 리스트에 숫자 더하기

def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            # j == 0 일때 -> 다음 줄로 내려갈 때도 index 0인 값에 누적
            if j == 0:
                triangle[i][j] += triangle[i-1][j]

            # j가 삼각형 한 행의 끝 인덱스일 때는 그 아랫줄의 끝값에 누적
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]

            # 그 외에는 -1 인덱스, +1 인덱스 중 최댓값 찾아서 더하기
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    # 맨 아랫줄에 나오는 누적값 중 최댓값 구하기
    answer = max(triangle[-1])
    return answer
