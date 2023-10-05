import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 3자리 이상일 경우 어떻게 나누어야 하는지 참고
# https://dalseoin.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-20164-%ED%99%80%EC%88%98-%ED%99%80%EB%A6%AD-%ED%98%B8%EC%84%9D
def findOdd(N):
    cnt = 0
    tmp = N
    while tmp:
        if tmp%2 == 1:
            cnt += 1
        tmp //= 10
    return cnt
ans = []
def operation(N, cnt):
    if len(str(N)) == 1:
        ans.append(cnt)
        return

    if len(str(N)) >= 3:
        for i in range(1, len(str(N))):
            for j in range(i+1, len(str(N))):
                num1 = int(str(N)[:i])
                num2 = int(str(N)[i:j])
                num3 = int(str(N)[j:])
                new = num1+num2+num3

                operation(new, cnt+findOdd(new))
    elif len(str(N)) == 2:
        new = (N//10) + (N%10)
        operation(new, cnt+findOdd(new))


N = int(input())
operation(N, findOdd(N))

print("{} {}".format(min(ans), max(ans)))
