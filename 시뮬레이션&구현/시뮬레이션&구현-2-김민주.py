# 함수로 과정 쪼개서 분할 연습
# 중간 오류 발생

import math
import sys
from itertools import combinations

input = sys.stdin.readline

num = input().rstrip()

# 함수 3개로 과정 분할

# 홀수 갯수 추출


def grab_odd(number):
    odds = 0
    for n in number:
        if int(n) % 2 == 1:
            odds += 1
    return odds

# 수 3개로 분할할 인덱스 조합 추출


def make_combination(number):
    li = [i for i in range(len(number)-1)]
    how_divide = list(combinations(li, 2))

    return how_divide

# 인덱스 추출 결과를 갖고, 수 분할 및 분할 결과를 더해서 홀수 갯수 추출 (재귀 포함)

# 인덱스 추출 결과와 number를 갖고 분할, 덧셈으로 결과값 추출


def divide_number(number, indexes):
    result = ['', '', '']

    for i in range(len(number)):
        if i <= indexes[0]:
            result[0] += number[i]
        if indexes[0] < i <= indexes[1]:
            result[1] += number[i]
        if i > indexes[1]:
            result[2] += number[i]

    result_sum = int(result[0]) + int(result[1]) + int(result[2])

    return result_sum


# 함수 다 조합시켜서 숫자 -> 인덱스조합 -> 숫자분할 -> 합쳐서 홀수 만들기 함수
# 함수를 통해 외부변수를 더해줄 때는 global로 외부변수를 가져와서 더해주기
odds = 0
results = []


def make_result(number):
    global odds
    index_list = make_combination(number)
    odds += grab_odd(number)
    for i in index_list:
        d = str(divide_number(number, i))
        print(d)
        # odds += grab_odd(d)
        print("지금까지 홀수 갯수: ", odds)

        if len(d) >= 3:
            make_result(d)
        else:

            while len(d) > 1:
                odds += grab_odd(d)
                new_num = int(d[0]) + int(d[1])
                d = str(new_num)

            if len(d) == 1:
                odds += grab_odd(d)
                results.append(odds)
                odds = 0


make_result(num)
print("결과값 모음: ", results)
# print("최종 홀수 갯수: ", odds)
print(min(results), max(results))


# 예시 코드 (https://tmdrl5779.tistory.com/139)

n = input()

min_v = math.inf
max_v = 0

# 홀수 갯수 판별 함수


def command1(n: str):
    odd_n = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_n += 1
    return odd_n


# 답 구하는 함수
def solve(n, odd_n):
    global max_v, min_v

    if len(n) == 1:
        min_v = min(min_v, odd_n)
        max_v = max(max_v, odd_n)
    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, odd_n + command1(temp))
    else:
        # 이중반복문으로 인덱스 2개를 움직여가며 슬라이싱하고, 슬라이싱 결과로 나온 수 3개를 더함
        # 수 3개를 더한 temp 값으로 solve 재귀 돌림
        for i in range(len(n) - 2):
            for j in range(i+1, len(n)-1):
                a = n[:i+1]
                b = n[i+1: j+1]
                c = n[j+1:]
                temp = str(int(a) + int(b) + int(c))
                solve(temp, odd_n + command1(temp))


solve(n, command1(n))
print(min_v, max_v)
