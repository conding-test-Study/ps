# 슬라이싱 + 원소 갯수 구하기 로 아이디어를 짠 건 좋았는데, 코드로 구현하는 것이 조금 꼬였음

import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
food = []
for _ in range(N):
    food.append(int(input()))

print(food)

# 줄세우기
bonus_if = []
for start in range(N):
    end = start + k
    if end <= N:
        li = food[start:end]
    else:
        li = food[start:N] + food[0:(end-N)]

    bonus_if.append(li.count(c))

a1 = k+1 - min(bonus_if)

# 줄 안 세우고 k개 뽑기 -> 가능한지 아닌지 기록
b = food.count(c)
if N - b >= k:
    a2 = k
    print(max(a1, a2))
else:
    print(a1)


# 코드 구현 관련하여 예시 참고함 (출처: https://lighter.tistory.com/92)
N, d, k, c = map(int, input().rstrip().split())
sushi = [int(input()) for _ in range(N)]
max_number_of_type = 0
for i in range(N):
    if i+k > N:
        number_of_type = len(set(sushi[i:N] + sushi[:(i+k) % N] + [c]))
    else:
        number_of_type = len(set(sushi[i:i+k] + [c]))
    if max_number_of_type < number_of_type:
        max_number_of_type = number_of_type
print(max_number_of_type)
