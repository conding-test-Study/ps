# 카운팅 로직 떠올리다가, 빈칸 발생 시의 사례를 예외처리할 방법을 몰라서 다른 답안 찾아봄
# 모범풀이는 갯수별 product + sort 로 해결 (출처: https://alreadyusedadress.tistory.com/297)

from itertools import product


def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1
