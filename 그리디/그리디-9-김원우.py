from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        w = people.pop()
        cnt = 1
        while people and w + people[0] <= limit and cnt < 2:
            w += people.popleft()
            cnt += 1
        answer += 1

    return answer

# 그리디 + 투포인터 문제같은 느낌?
# 최대 2명까지 탑승 할 수 있기 때문에 제일 무거운놈 + 제일 가벼운놈 조합으로 태워야 최적해다