from itertools import permutations

# 소수 찾기 함수
# n을 2부터 n-1까지 순차적으로 나눠서 그 무엇으로도 나눠지지 않으면 소수라고 판정


def find_prime_number(n):
    if n == 0 or n == 1:
        return False

    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# '소수 찾기 함수'에 집어넣은 후보 수를 permutations로 찾기


def make_number(x, i):
    result = []
    ns = permutations(x, i)

    for n in ns:
        r = ''

        for j in range(i):
            r += n[j]

        result.append(int(r))

    return result


def solution(numbers):

    nums = []
    for i in range(1, len(numbers)+1):

        # permutations로 숫자 뽑기
        re = make_number(numbers, i)

        # 소수 판별하기
        for r in re:
            if find_prime_number(r) == True:
                nums.append(r)

    # 중복 제거
    answer = len(set(nums))
    return answer
