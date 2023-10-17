def solution(sizes):

    for s in sizes:
        s.sort()

    s1 = []
    s2 = []
    for s in sizes:
        s1.append(s[0])
        s2.append(s[1])

    answer = max(s1) * max(s2)
    return answer
