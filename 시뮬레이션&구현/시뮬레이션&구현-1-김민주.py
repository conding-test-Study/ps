# 문제의 지시사항을 어느 정도 구현해보려 했으나, 전부 구현하는 데 실패함
from collections import defaultdict
import sys
N = int(input())

students = []
graph = []
for i in range(N**2):
    a, b, c, d, e = map(int, input().split())
    students.append([a, b, c, d, e])

for i in range(N):
    graph.append([0 for _ in range(N)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    me = student[0]
    print(me)
    student.remove(me)

    love_person = []
    # for s in student:
    for i in range(N):
        for j in range(N):
            # 포함관계
            if graph[i][j] in student:
                love_person.append((i, j))

    print(love_person)

    if len(love_person) == 0:
        graph[1][1] = me

    print(graph)

# 이하는 예시 코드 (출처: https://jaehwaseo.tistory.com/23)

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
n = int(sys.stdin.readline())
seats = [[0] * n for _ in range(n)]
students = [list(map(int, sys.stdin.readline().split()))
            for _ in range(n ** 2)]
friends = defaultdict(set)
for student in students:
    me = student[0]
    friends[me] = set(student[1:])
    possible = []

    # 그래프 탐색
    for x in range(n):
        for y in range(n):

            # empty, friend 별개 변수 생성
            if not seats[x][y]:
                empty = 0
                friend = 0
                # seats 그래프 인덱스로 탐색
                for _ in range(4):
                    nx = rx[_] + x
                    ny = ry[_] + y
                    if 0 <= nx < n and 0 <= ny < n:
                        # 그래프에 착석자 수와 빈자리 수를 구별하여 변수 늘리기
                        if not seats[nx][ny]:
                            empty += 1
                        if seats[nx][ny] in friends[me]:
                            friend += 1
                possible.append((friend, empty, x, y))

    # 람다 정렬 이후, 정렬된 첫 번째 원소의 좌표에 자리 배치 시행
    # 친구가 가장 많이 앉아 있는 그 포인트에 자리 배치
    # possible 원소 만드는 과정에서 문제에 제시된 요건 전부 다 처리하도록 구성
    possible.sort(key=lambda k: (-k[0], -k[1], k[2], k[3]))
    _, _, x, y = possible[0]
    seats[x][y] = me

# 만족도 구하기
answer = 0
for x in range(n):
    for y in range(n):
        me = seats[x][y]
        friend = 0
        for _ in range(4):
            nx = rx[_] + x
            ny = ry[_] + y
            if 0 <= nx < n and 0 <= ny < n:
                if seats[nx][ny] in friends[me]:
                    friend += 1
        if friend:
            answer += 10 ** (friend - 1)

print(answer)
