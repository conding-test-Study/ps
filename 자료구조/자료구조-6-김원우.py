# 브루트포스가 아닌 스택/큐를 이용하여 푸는 풀이를 떠올리지 못함
# 답지 참고 함

def solution(prices):
    answer = [0]*len(prices)
    stack = []

  # 가격을 스택에 넣다가 스택의 top에 있는 가격보다 prices에서 꺼낸 가격이 작을때를 캐치
  # 이후 while 루프를 돌면서 인덱스의 차이를 이용하여 answer 배열 갱신
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
  # 값이 떨어지지 않고 순회가 끝났을 경우 스택의 남은 값들을 통해 answer 배열 갱신 
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer
