# 덱을 이용하여 풀어보려고 했으나, 다양한 반례에 따라 예외사항을 마련하게 되는 과정에서 풀이 방향이 잘못되었음을 알게 됨
# 반례 모음: https://www.acmicpc.net/board/view/107573

import sys
from collections import deque

input = sys.stdin.readline


def make_profit(prices, num):

    D = deque()
    profit = 0

    # 주가가 전날보다 같거나 높으면 덱에 넣기, 그렇지 않으면 (덱[-1] - 나머지원소) 연산하기
    for n in range(num):
        if n == 0:
            D.append(prices[n])
        else:
            if prices[n] >= prices[n - 1]:
                D.append(prices[n])
            else:
                print("현재의 덱: ", D)
                if len(D) > 1:
                    std = D.pop()
                    while D:
                        a = D.popleft()
                        if std > a:
                            profit += std - a
                D.append(prices[n])

    if len(D) > 0:
        print("현재의 덱: ", D)
        std = D.pop()
        while D:
            a = D.popleft()
            if std > a:
                profit += std - a

    if profit <= 0:
        profit = 0

    return profit


T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    result = make_profit(prices, N)
    print(result)

# 모범 접근: 주가 리스트를 뒤에서부터 돌린 뒤, 최댓값이 나오면 그 최댓값과 이외 주식의 가격 차를 연산
# 출처: https://amor-fati.tistory.com/51
input = sys.stdin.readline


def get_profit(n, price):
    profit = 0      # 최대 이익
    max_price = price[-1]
    for i in range(n-2, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    print(profit)


t = int(input())   # 테스트케이스 개수
for _ in range(t):
    n = int(input())   # 날의 수
    price = list(map(int, input().split()))   # 날 별 주가
    get_profit(n, price)
