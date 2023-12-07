#답지 확인
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                bigger = max(triangle[i-1][j], triangle[i-1][j-1])
                triangle[i][j] += bigger

    return max(triangle[len(triangle) - 1])

#.
#|\  1층까지 최대값일 때 좌표와 값  이떄 최대 아닌 좌표로 내려갔을때 최대 값이 나올 수있음
#|.\  그래서 끝까지 내려가봐야 알 수 있다? 처음 완탐DFS가 떠올랐는데 시간초과를 어떻게 알지?
#|..\  왜 DP? 지금까지의 숫자로 DP?     내려온 층을 가지고 DP?  X 2층최대를 갖고 더해서 3층을 만드는게 아님
#.....    지금까지의 숫자로 DP? 15만든게 2층이네  18만든게 3층이네  다 하나 씩 탐색해보려면 DFS아닌가

#https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95
#dp테이블을 만들지 않고 triangle에서 아래로 내려가면서 더해주면서 누적된 합을 저장한다. 
#누적 합을 구할때 가장 큰 값이 오는 경우로 하기 위해 위에 왼쪽 오른쪽중 더 큰 값을 선택해서 더한다? 
#맨 아래에서 최대 값을 구한다.
