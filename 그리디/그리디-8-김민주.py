# 풀이 출처: https://chiefcoder.tistory.com/37
# 스택을 이용한 구현

def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])
