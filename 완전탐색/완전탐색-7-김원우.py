# permutations 쓰면 간단하게 풀기 가능
# 중복되는 숫자에 대한 반례가 있으므로 set 활용

from itertools import permutations

def solution(numbers):
    answer = []

    tmp = [i for i in numbers]
    num = []

    for i in range(1, len(tmp) + 1):
        num += list(permutations(tmp, i))
    newnum = [int("".join(p)) for p in num]
    print(newnum)
    for n in newnum:
        if n == 0 or n == 1:
            continue
        cnt = 0
        for i in range(1, n + 1):
            if cnt > 2:
                break
            if n % i == 0:
                cnt += 1

        if cnt == 2:
            answer.append(n)

    return len(set(answer))