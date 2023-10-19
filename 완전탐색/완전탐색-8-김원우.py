# 순열이랑 조건만으로 풀 수 있음

from itertools import permutations

def solution(brown, yellow):
    answer = []

    s = brown + yellow

    tmp = []
    for i in range(1, s + 1):
        if s % i == 0:
            tmp.append(i)
            if i * i == s:
                tmp.append(i)
    carpet = list(permutations(tmp, 2))
    for w, h in carpet:
        if w * h != s:
            continue
        if w < h:
            continue
        elif h < 3:
            continue
        elif (w - 2) * (h - 2) != yellow:
            continue

        if w not in answer:
            answer.append(w)
            answer.append(h)

    print(answer)
    return answer